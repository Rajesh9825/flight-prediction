# Flight Price Prediction

##  Problem Statement

Flight ticket prices fluctuate based on various factors such as airline, time of booking, demand, number of stops, and seasonal trends. The goal of this project is to build a machine learning model that can accurately predict flight prices based on historical data. Additionally, a user-friendly web application is developed to allow users to input their flight details and get a price prediction.

##  Expected Outcomes

- Develop a robust machine learning model to predict flight ticket prices.
- Perform thorough data analysis to identify key factors affecting price variations.
- Build a web application for real-time flight price predictions.
- Successfully deploy the application while addressing challenges like large model size and free hosting limitations.

---

## 📁 Project Structure

```
Flight_Price_Prediction/
│-- artifacts/ 
|   |-- data.csv
|   |-- preprocessor.pkl
|   |-- test.csv
|   |-- train.csv
|-- data/                     # Contains dataset files
|   |-- Dataset
│-- notebooks/                 # Jupyter notebooks for EDA & model training
│-- src/
|   |-- components
|   |   |-- data_ingestion.py   
|   |   |-- data_transformation.py   
|   |   |-- model_trainer.py   
|   |-- pipeline
|   |   |-- predict_pipeline.py  
|   |-- exception.py
|   |-- logger.py
|   |-- utils.py    
│-- templates/                 # HTML files for web app
|   |-- index.html  
|-- .gitignore               
│-- application.py             # Flask backend for prediction
|-- Dockerfile
|-- huggingfacemodel.py
│-- requirements.txt           # Dependencies for running the project
│-- README.md                  # Project documentation
<!-- │-- deployment/                # Files related to Hugging Face deployment -->
```

---


## 🔍 Project Workflow

### 1️. Data Collection & Loading

- Loaded a structured dataset containing flight prices, airlines, sources, destinations, and timestamps.
- Used **Pandas** and **NumPy** for data manipulation and preprocessing.

### 2. Data Exploration & Cleaning

- Checked for missing values and handled them appropriately.
- Extracted useful information from date-time columns (e.g., extracting month, day, and time slots).
- Identified and removed duplicates or inconsistencies in the dataset.

### 3. Exploratory Data Analysis (EDA)

- Visualized trends using Seaborn and Matplotlib.
- Identified how factors like airline, number of stops, departure time, and travel duration impact prices.
- Used correlation heatmaps and boxplots to understand feature importance.

### 4️. Feature Engineering 

- Applied One-Hot Encoding to convert categorical variables into numerical values.
- Created additional features like "Days Until Departure" and "Journey Duration" to enhance model performance.
- Standardized numerical values to ensure smooth model training.

### 5. Model Selection & Training

- Implemented various models to compare performance:
  - **Baseline Model:** Linear Regression
  - **Other Models:** K-Nearest Neighbors (KNN), Decision Tree, Random Forest, Gradient Boosting, XGBoost
- Evaluated models using:
  - **Mean Absolute Error (MAE)**
  - **Mean Squared Error (MSE)**
  - **R-squared Score (R²)**
- Selected **Random Forest** as the best-performing model based on evaluation metrics.

### 6. Challenges Faced & Solutions

#### Challenge: Large Model File Size

**Problem:**
- The trained model file exceeded GitHub's file size limit.
**Solution:**
- Used **Hugging Face Model Hub** to store the model and loaded it dynamically in the web app using API calls.

#### Challenge: Deployment on Render

**Problem:**
- Render had file upload restrictions, preventing direct deployment.
**Solution:**
- Deployed the entire web application on **Hugging Face Spaces** for seamless access and execution.

### 7️. Web Application Development & Deployment

- Built an interactive Flask-based web app.
- Created a responsive UI using HTML, CSS, and JavaScript.
- Integrated model inference API to allow real-time predictions.
- Successfully deployed the application on Hugging Face Spaces.

Live Demo : 
---
