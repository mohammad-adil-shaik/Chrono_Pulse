# CHRONO-PULSE AI --- AI-Powered Sleep Disorder Prediction System

Chrono-Pulse AI is a **web-based machine learning application** that
predicts potential sleep disorders---such as **Insomnia**, **Sleep
Apnea**, or **No Disorder**---based on lifestyle, sleep patterns, and
health data.

Powered by Gradient Boosting (96% accuracy)\
Modern React UI\
Real-time Health Score\
No signup, no data storage\
Fully deployed on free-tier services (Render + Vercel)


## **Live Demo**

🔗 **Frontend:** https://chronopulse-frontend.vercel.app\
🔗 **Backend API Docs:** https://chronopulse-backend-1.onrender.com/docs






# **Features**

-   **AI-Powered Predictions** using Gradient Boosting (96% accuracy)
-   **User-Friendly Interface** with responsive UI
-   **Real-Time Health Score** updates as users fill the form
-   **Personalized Health Recommendations**
-   **Zero Data Storage** -- complete privacy
-   **100% Free to Use** -- hosted on free-tier platforms



# **Technology Stack**

### **Frontend**

-   React.js 18.2.0\
-   Axios\
-   CSS3 with animations\
-   Hosted on **Vercel**

### **Backend**

-   FastAPI 0.115.0\
-   Python 3.11.9\
-   Scikit-learn 1.6.1\
-   Uvicorn server\
-   Hosted on **Render**

### **Machine Learning**

-   Algorithm: **Gradient Boosting Classifier**\
-   Dataset Size: 374 records\
-   Features: 23 variables\
-   Classes: No Disorder, Insomnia, Sleep Apnea



# **Project Structure**

    chrono-pulse-ai/
    ├── backend/
    │   ├── main.py               # FastAPI application
    │   ├── requirements.txt      # Python dependencies
    │   ├── runtime.txt           # Python version
    │   ├── best_model.pkl        # Trained ML model
    │   ├── scaler.pkl            # Feature scaler
    │   ├── feature_names.pkl     # List of feature names
    │   └── model_info.pkl        # Model metadata
    │
    ├── frontend/
    │   ├── public/               # Static assets
    │   ├── src/
    │   │   ├── App.jsx           # Main React component
    │   │   ├── App.css           # Styling
    │   │   └── index.js          # Entry point
    │   ├── package.json
    │   └── .gitignore
    │
    └── README.md



# **Installation & Setup**

## **Prerequisites**

-   Python 3.11+
-   Node.js 16+
-   Git



# **Backend Setup**

``` bash
git clone https://github.com/mohammad-adil-shaik/chronopulse-backend-1
cd chronopulse-backend-1
pip install -r requirements.txt
uvicorn main:app --reload
```

Server will start at:

👉 **http://localhost:8000**



# **Frontend Setup**

``` bash
git clone https://github.com/mohammad-adil-shaik/chronopulse-frontend
cd chronopulse-frontend
npm install
```

Update API URL in `src/App.jsx`:

``` javascript
const API_URL = 'http://localhost:8000';
```

Run the app:

``` bash
npm start
```

Open: **http://localhost:3000**



# **Dependencies**

## **Backend (requirements.txt)**

    fastapi==0.115.0
    uvicorn[standard]==0.32.0
    scikit-learn==1.6.1
    pandas==2.2.3
    numpy==2.0.2
    python-multipart==0.0.12
    pydantic==2.10.3

## **Frontend (package.json)**

``` json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.2",
    "lucide-react": "^0.294.0"
  }
}
```



# **How to Run**

### **Option 1 --- Use Live Deployment**

https://chronopulse-frontend.vercel.app

### **Option 2 --- Run Locally**

#### 1️⃣ Start Backend

``` bash
cd backend
uvicorn main:app --reload
```

#### Start Frontend

``` bash
cd frontend
npm start
```

#### 3️⃣ Go to

👉 **http://localhost:3000**



# **Usage Guide**

1.  Open the app\
2.  Fill in details (sleep, lifestyle, health metrics)\
3.  Click **Analyze Sleep Health**\
4.  Wait 2--3 seconds (or 30--60 seconds on cold start)\
5.  View predictions + recommendations



# **Deployment Details**

### **Backend --- Render**

-   URL: https://chronopulse-backend-1.onrender.com\
-   Cold Start: 30--60 sec\
-   Auto-deploy on push to `main`

### **Frontend --- Vercel**

-   URL: https://chronopulse-frontend.vercel.app\
-   Instant CDN loading\
-   Auto-deploy from GitHub

------------------------------------------------------------------------

# **Testing**

### **Backend Docs**

https://chronopulse-backend-1.onrender.com/docs

### **Sample Input**

    Age: 30
    Gender: Male
    Sleep Duration: 7
    Quality of Sleep: 7
    Stress Level: 5
    Physical Activity: 60
    Daily Steps: 7000
    Heart Rate: 70
    Blood Pressure: 120/80



# Important Notes

-   Not a medical device\
-   Free tier backend sleeps after inactivity\
-   No personal data stored\
-   Internet required



# Troubleshooting

  Issue                 Fix
   
  Backend unavailable   Wait for cold start
  Prediction error      Check browser console
  Slow results          First call only
  Local errors          Check Python + Node versions



# License

Academic project (2025) -- **Team 5**\
All Rights Reserved



# Project Stats

-   **2500+ lines of code**\
-   **6 weeks development**\
-   **5 members**\
-   **96% accuracy**\
-   **\$0/month deployment**
