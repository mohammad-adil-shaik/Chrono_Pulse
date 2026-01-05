from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
from typing import List, Dict, Any

# Initialize FastAPI app
app = FastAPI(
    title="Chrono-Pulse AI API",
    description="Sleep Disorder Prediction API",
    version="1.0.0"
)

# CORS middleware to allow React frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - we'll restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model and related files
try:
    with open('best_model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    with open('feature_names.pkl', 'rb') as file:
        feature_names = pickle.load(file)
    with open('model_info.pkl', 'rb') as file:
        model_info = pickle.load(file)
    print("✓ All model files loaded successfully!")
except Exception as e:
    print(f"✗ Error loading model files: {e}")
    model = None

# Pydantic models for request/response
class PredictionInput(BaseModel):
    age: int
    gender: str
    occupation: str
    sleep_duration: float
    quality_of_sleep: int
    physical_activity_level: int
    stress_level: int
    bmi_category: str
    heart_rate: int
    daily_steps: int
    systolic_bp: int
    diastolic_bp: int

class PredictionOutput(BaseModel):
    prediction: str
    confidence: Dict[str, float]
    recommendations: List[str]
    model_info: Dict[str, Any]

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to Chrono-Pulse AI API",
        "version": "1.0.0",
        "status": "active"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

# Model info endpoint
@app.get("/model-info")
def get_model_info():
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    return {
        "model_name": model_info['model_name'],
        "accuracy": model_info['accuracy'],
        "precision": model_info['precision'],
        "recall": model_info['recall'],
        "f1_score": model_info['f1_score'],
        "classes": model_info['classes']
    }

# Prediction endpoint
@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    try:
        # Prepare input data
        data = {
            'Age': input_data.age,
            'Sleep Duration': input_data.sleep_duration,
            'Quality of Sleep': input_data.quality_of_sleep,
            'Physical Activity Level': input_data.physical_activity_level,
            'Stress Level': input_data.stress_level,
            'Heart Rate': input_data.heart_rate,
            'Daily Steps': input_data.daily_steps,
            'Systolic_BP': input_data.systolic_bp,
            'Diastolic_BP': input_data.diastolic_bp,
        }
        
        # Gender encoding
        data['Gender_Male'] = 1 if input_data.gender == 'Male' else 0
        
        # Occupation encoding (one-hot)
        occupations = ['Accountant', 'Doctor', 'Engineer', 'Lawyer', 'Manager',
                      'Nurse', 'Sales Representative', 'Salesperson', 'Scientist',
                      'Software Engineer', 'Teacher']
        for occ in occupations[1:]:
            data[f'Occupation_{occ}'] = 1 if input_data.occupation == occ else 0
        
        # BMI Category encoding (one-hot)
        bmi_categories = ['Normal', 'Normal Weight', 'Obese', 'Overweight']
        for bmi in bmi_categories[1:]:
            data[f'BMI Category_{bmi}'] = 1 if input_data.bmi_category == bmi else 0
        
        # Create DataFrame
        input_df = pd.DataFrame([data])
        
        # Ensure all features are present
        for feature in feature_names:
            if feature not in input_df.columns:
                input_df[feature] = 0
        
        # Reorder columns
        input_df = input_df[feature_names]
        
        # Scale the input
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        # Create confidence dictionary
        confidence = {
            cls: float(prob * 100) 
            for cls, prob in zip(model.classes_, prediction_proba)
        }
        
        # Generate recommendations
        recommendations = generate_recommendations(input_data)
        
        return PredictionOutput(
            prediction=prediction,
            confidence=confidence,
            recommendations=recommendations,
            model_info={
                "model_name": model_info['model_name'],
                "accuracy": model_info['accuracy']
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

def generate_recommendations(data: PredictionInput) -> List[str]:
    """Generate personalized health recommendations"""
    recommendations = []
    
    if data.sleep_duration < 7:
        recommendations.append("⏰ Aim for 7-9 hours of sleep per night for optimal health")
    
    if data.quality_of_sleep < 6:
        recommendations.append("🛏️ Focus on improving sleep quality - maintain a consistent sleep schedule")
    
    if data.stress_level > 6:
        recommendations.append("🧘 Practice stress management techniques like meditation, yoga, or deep breathing")
    
    if data.physical_activity_level < 30:
        recommendations.append("🏃 Increase physical activity to at least 30 minutes of moderate exercise daily")
    
    if data.daily_steps < 5000:
        recommendations.append("👟 Try to achieve at least 7,000-10,000 steps per day")
    
    if data.heart_rate > 90:
        recommendations.append("💓 Monitor your heart rate - consult a doctor if it remains consistently elevated")
    
    if data.systolic_bp > 130 or data.diastolic_bp > 85:
        recommendations.append("🩺 Your blood pressure is elevated - please consult a healthcare provider")
    
    if not recommendations:
        recommendations.append("✨ Your health metrics look good! Keep up the healthy habits")
    
    return recommendations

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)