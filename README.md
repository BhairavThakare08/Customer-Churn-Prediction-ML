# 🚀 Customer Churn Prediction System

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Project-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-Deployed-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge">
</p>

<p align="center">
  <b>💡 End-to-End Machine Learning Project with Interactive Dashboard</b><br>
  <i>Predict customer churn with explainable insights & business-driven analytics</i>
</p>

---

## 🌐 Live Demo

🚀 **Try the Application Here:**  
👉 https://customer-churn-prediction-ml-twn4jqffobew3k3jqrlipe.streamlit.app/

---

## 📸 Dashboard Preview

<p align="center">
  <img src="images/dashboard1.png" width="80%">
  <br><br>
  <img src="images/dashboard2.png" width="80%">
</p>

---

## 📌 Project Overview

This project delivers a **production-ready Machine Learning solution** for predicting customer churn.

It integrates:
- 📊 **Multiple ML models**
- ⚙️ **Advanced preprocessing & feature engineering**
- 🎯 **Business-focused evaluation metrics**
- 🌐 **Interactive Streamlit dashboard**

💡 The system not only predicts churn but also provides **actionable insights** to support strategic business decisions.

---

## 🎯 Key Features

- ⚡ **Real-Time Churn Prediction**
- 📊 **Interactive Data Dashboard**
- 📉 **Churn Probability Visualization**
- 🧠 **Customer Risk Analysis**
- 📈 **Business Insights & Recommendations**

---

## 🧠 Machine Learning Pipeline

### 🔹 Models Implemented

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Support Vector Machine (SVM)

### 🔹 Techniques Applied

- Data Cleaning & Missing Value Handling  
- Feature Encoding (Label & One-Hot Encoding)  
- Feature Scaling (StandardScaler)  
- Feature Selection  
- Train-Test Split  
- Hyperparameter Optimization (RandomizedSearchCV)

---

## 📊 Model Performance Comparison  

| Model               | Accuracy | F1 Score | Recall |
|---------------------|----------|----------|--------|
| Logistic Regression | 0.74     | 0.62     | 0.81   |
| KNN                 | 0.76     | 0.54     | 0.53   |
| Decision Tree       | 0.77     | 0.58     | 0.60   |
| SVM                 | 0.72     | 0.61     | 0.82   |

---

## 🏆 Best Model Selection Strategy

Unlike typical projects that focus only on **Accuracy**, this system prioritizes:

- ✅ **Recall** → To minimize false negatives (missing churn customers)
- ✅ **F1-Score** → Balance between precision & recall

📌 **Final Model:** Logistic Regression  
✔️ Best trade-off between performance & interpretability  
✔️ Suitable for real-world business deployment  

---

## 🧩 Input Features

Key attributes used for prediction:

- 👤 Customer Demographics (Gender, Senior Citizen)
- ⏳ Account Information (Tenure, Contract Type)
- 💰 Billing Details (Monthly Charges, Total Charges)
- 🌐 Services (Internet Service, Tech Support, Security)

---

## 🛠️ Tech Stack

| Category       | Tools Used         |
|--------------- |--------------------|
| Programming    | Python             |
| Data Handling  | Pandas, NumPy      |
| ML Models      | Scikit-learn       |
| Visualization  | Matplotlib, Altair |
| Deployment     | Streamlit          |

---

## 💡 Business Impact

This solution enables organizations to:

- 🎯 Identify high-risk customers early  
- 📉 Reduce churn rate  
- 💰 Increase customer retention  
- 📊 Make data-driven strategic decisions  

---

## ⚙️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/customer-churn-prediction.git

# Navigate to project folder
cd customer-churn-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
