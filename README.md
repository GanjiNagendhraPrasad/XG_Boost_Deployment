<h1 align="center">XG Boost Deployment</h1>

<p align="center">
  An interactive web app that uses the XGBoost machine learning model to predict breast cancer diagnosis from user-provided features. The model is trained on medical diagnostic data and deployed as an easy-to-use browser interface.
</p>

---

## 🚀 **Live Demo**

👉 Visit the deployed app here:  
<a href="https://xg-boost-deployment.onrender.com/" target="_blank">https://xg-boost-deployment.onrender.com/</a>

You can enter diagnostic features related to breast tumor measurements and get an immediate prediction of whether the tumor is likely to be **benign** or **malignant**.

---

## 🧠 **About the Project**

This project implements a **machine learning classification model** using **Extreme Gradient Boosting (XGBoost)** — one of the state-of-the-art ML algorithms used for structured/tabular data. XGBoost is known for its high accuracy and performance on classification tasks, especially when dealing with medical or diagnostic datasets. :contentReference[oaicite:0]{index=0}

The main purpose of this project is to **predict the diagnosis of breast cancer** using clinical features from the **Breast Cancer Wisconsin dataset** through an intuitive web interface.

---

## 🧪 **How It Works**

### 🧩 Data
- The dataset contains 30 numerical diagnostic measurements (such as *radius mean*, *texture mean*, *area mean*, *concavity mean*, etc.) for breast tumors.
- These features are widely used in breast cancer prediction models. :contentReference[oaicite:1]{index=1}

---

### ✨ Model: XGBoost
- XGBoost is an optimized implementation of gradient boosting machines that builds an ensemble of decision trees sequentially.
- Each new tree corrects the errors of the previous trees to improve prediction performance.
- XGBoost is fast and scalable, with strong results in health-related classification problems. :contentReference[oaicite:2]{index=2}

---

### 🧪 Training Process
The core model pipeline includes:
1. **Loading and preprocessing the Breast Cancer dataset**
2. **Splitting the data** into training and test sets
3. **Training an XGBoost classifier**
4. **Evaluating the model performance**
5. **Saving the trained model as `xgb.pkl`**

This saved model file is then used by the web app to generate live predictions without retraining.

---

## 🌐 **Web App Architecture**

The project contains:

📌 `app.py`  
- A Flask server that handles HTTP requests  
- Loads the pre-trained XGBoost model (`xgb.pkl`)  
- Renders HTML templates  
- Performs prediction on user input  

📌 `templates/`  
- HTML files for user interface  
- Take raw user input and send back prediction results

📌 `requirements.txt`  
- Lists all Python dependencies needed to run the project

📌 Deployment config (`Procfile`, etc.)  
- Enables deployment on cloud platforms like Render

---

## 🖥️ User Interface

When users visit the live app:

➡ A form displays all relevant numerical features corresponding to tumor characteristics such as:

- Radius Mean  
- Texture Mean  
- Perimeter Mean  
- Area Mean  
- Smoothness Mean  
- Compactness Mean  
- … and others  

Users enter values for these features and click **Predict Diagnosis** to get a result of either *Benign* or *Malignant*. (Example backend interface shown here.) :contentReference[oaicite:3]{index=3}

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python (Flask) |
| ML Model | XGBoost |
| Frontend UI | HTML / Bootstrap |
| Deployment | <a href="https://render.com" target="_blank">Render</a> |
| Data Processing | pandas / scikit-learn |

---

## 📦 How to Run Locally

Clone the repository and run:

```bash
git clone https://github.com/GanjiNagendhraPrasad/XG_Boost_Deployment.git
cd XG_Boost_Deployment
pip install -r requirements.txt
python app.py
