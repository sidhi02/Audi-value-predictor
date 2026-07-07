<h1 align="center">Audi Car Price Predictor</h1>

<p align="center">
  <strong>AI-powered web application for predicting the market value of Audi vehicles using Random Forest Regression.</strong>
</p>

<p align="center">
  Estimate your Audi's resale value instantly using machine learning trained on real-world vehicle data.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Live-28a745">
</p>

<p align="center">
  <a href="https://your-render-url.onrender.com">
    <img src="https://img.shields.io/badge/Live%20Demo-Visit%20Application-C8102E?style=for-the-badge">
  </a>
</p>

---

## 📸 Preview

<p align="center">
  <img src="images/preview.png" alt="Audi Car Price Predictor" width="100%">
</p>

---

## ✨ Features

- Predicts the market value of Audi vehicles instantly
- Machine Learning model powered by **Random Forest Regression**
- Trained on real-world Audi vehicle listings
- Automatic **GBP → INR** price conversion
- Modern, responsive Audi-inspired user interface
- Fast prediction with Flask backend
- Deployed on Render

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Backend** | Flask, Python |
| **Machine Learning** | Scikit-learn, Random Forest Regression |
| **Data Processing** | Pandas, NumPy |
| **Model Persistence** | Joblib |
| **Deployment** | Render, Gunicorn |

---

## 📂 Project Structure

```text
Audi-Car-Price-Predictor/
│
├── app.py
├── audi_price_model.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── audi.jpg
│   └── audi-logo.png
│
└── images/
    └── preview.png
```

---

## 📊 Input Features

The prediction model uses the following vehicle specifications:

- Model
- Manufacturing Year
- Transmission
- Fuel Type
- Mileage
- Fuel Efficiency
- Engine Size

---

## 🧠 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Feature Engineering
   │
   ▼
One-Hot Encoding
   │
   ▼
Train-Test Split
   │
   ▼
Random Forest Regression
   │
   ▼
Model Evaluation
   │
   ▼
Model Serialization (Joblib)
   │
   ▼
Flask Web Application
   │
   ▼
Deployment on Render
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/Audi-value-predictor.git
cd Audi-value-predictor
```

### Create a Virtual Environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Your Browser

```
http://127.0.0.1:5000
```

---

## 📈 Model Information

| Model | Random Forest Regression |
|------|---------------------------|
| Target Variable | Price |
| Framework | Scikit-learn |
| Prediction | Estimated Audi Market Value |

---

## 🔮 Future Improvements

- Support for multiple car brands
- Live market price integration
- Price trend visualization
- Prediction confidence score
- REST API
- User authentication and prediction history

---

## 👨‍💻 Author

**Sidhi Deshmukh**

Aspiring Data Analyst and Machine Learning Enthusiast passionate about building intelligent, data-driven applications.

- GitHub: [(https://github.com/sidhi02/Audi-value-predictor)]
---

