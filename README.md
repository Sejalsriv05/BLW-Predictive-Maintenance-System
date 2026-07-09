

# 🚂 AI-Based Predictive Maintenance Scheduling System

An AI-powered Predictive Maintenance Scheduling System developed during my Industrial Training at **Banaras Locomotive Works (BLW), Varanasi**.

The application predicts machine failure probability using Machine Learning, calculates a health score, recommends maintenance schedules, and provides an interactive dashboard for maintenance monitoring.

---

# Project Overview

Traditional maintenance methods often lead to:

- Unexpected machine failures
- High maintenance costs
- Increased downtime
- Reduced production efficiency

This project uses a Machine Learning model to predict equipment health based on operational parameters and automatically schedules maintenance before breakdowns occur.

---

# Features

- Predicts machine failure probability
- Calculates machine health score
- Generates maintenance priority
- Recommends maintenance date
- Saves maintenance history
- Interactive maintenance dashboard
- Attractive Streamlit web interface
- Machine-wise maintenance tracking

---

# Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Random Forest Classifier

### Frontend

- Streamlit

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Plotly

### Model Storage

- Joblib

---

# Dataset

The project uses the **AI4I 2020 Predictive Maintenance Dataset**.

Features used include:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

These parameters are used to predict machine failure probability.

---

# System Workflow

Input Machine Parameters

↓

Random Forest Model

↓

Failure Probability Prediction

↓

Health Score Calculation

↓

Risk Assessment

↓

Maintenance Recommendation

↓

Dashboard Storage

---

# Screenshots

## Home Page

<img width="1467" height="814" alt="Screenshot 2026-07-09 at 1 09 38 PM" src="https://github.com/user-attachments/assets/6b39cec2-5c24-4c63-9589-d1003b80e62f" />


---

## Predictor Page

<img width="1470" height="869" alt="Screenshot 2026-07-09 at 1 11 01 PM" src="https://github.com/user-attachments/assets/a609639b-226f-4c52-ab08-5d5294c51021" />


---

## Prediction Result

 <img width="1453" height="815" alt="Screenshot 2026-07-09 at 1 14 06 PM" src="https://github.com/user-attachments/assets/5b6f71f6-ada0-47f4-b792-21130963c256" />



---

## Dashboard

<img width="1470" height="574" alt="Screenshot 2026-07-09 at 1 15 07 PM" src="https://github.com/user-attachments/assets/78dd6614-609a-4e68-8c97-174649b48221" />
<img width="1459" height="691" alt="Screenshot 2026-07-09 at 1 15 35 PM" src="https://github.com/user-attachments/assets/8177ae85-71e2-4816-ac19-de94c336992b" />


---

## Charts

<img width="1406" height="469" alt="Screenshot 2026-07-09 at 1 18 00 PM" src="https://github.com/user-attachments/assets/658348af-f4de-4c43-8906-5443ba5d8958" />


---

# Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Why Random Forest?

- High Accuracy
- Handles Non-linear Data
- Less Overfitting
- Fast Prediction
- Robust Performance

---

# Project Structure

```text
BLW-Predictive-Maintenance-System
│
├── app.py
├── model
│   └── random_forest_model.pkl
│
├── output
│   └── maintenance_results.csv
│
├── screenshots
│
├── ai4i2020.csv
├── requirements.txt
└── README.md



# Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Why Random Forest?

- High Accuracy
- Handles Non-linear Data
- Less Overfitting
- Fast Prediction
- Robust Performance

---

---

# Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/BLW-Predictive-Maintenance-System.git
```

### Navigate to the Project Directory

```bash
cd BLW-Predictive-Maintenance-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The application will start on your local machine. Open the URL displayed in the terminal (typically `http://localhost:8501`) in your web browser.

---

# Future Enhancements

This project can be further improved by incorporating advanced Industry 4.0 technologies and additional predictive maintenance features.

- IoT sensor integration for real-time data collection
- Live machine health monitoring
- Email notification system
- SMS alerts for critical failures
- Cloud deployment using AWS or Azure
- Power BI integration for business analytics
- Deep Learning-based prediction models
- Remaining Useful Life (RUL) prediction
- Automated maintenance scheduling
- Multi-user authentication
- Mobile-friendly dashboard
- Integration with industrial PLC and SCADA systems

---

# Learning Outcomes

This project provided practical exposure to the following concepts:

- Industrial Predictive Maintenance
- Machine Learning Model Development
- Random Forest Classification
- Data Preprocessing and Feature Engineering
- Streamlit Web Application Development
- Dashboard Design and Data Visualization
- Industrial Data Analysis
- Model Deployment using Joblib
- Git and GitHub Project Management
- AI Applications in Manufacturing Industries

---

# Industrial Training

This project was developed during my Industrial Training at:

**Banaras Locomotive Works (BLW)**  
Varanasi, Uttar Pradesh, India

During the training, I gained practical exposure to:

- CNC Machine Shop
- Loco Test Shop (LTS)
- Engineering Design and Planning (EDP)
- Industrial Maintenance Practices
- Predictive Maintenance Concepts
- Machine Learning Applications in Manufacturing

The experience gained during the training inspired the development of this AI-Based Predictive Maintenance Scheduling System.

---

# Author

**Sejal Srivastava**

B.Tech in Computer Science and Engineering  
VIT Bhopal University

GitHub: https://github.com/Sejalsriv05

LinkedIn: https://www.linkedin.com/in/sejalsrivastava05/

Email: sejalsriv2005@gmail.com
---

# License

This project has been developed for educational, research, and industrial training purposes.

It demonstrates the application of Machine Learning techniques for predictive maintenance and maintenance scheduling in an industrial environment.

© 2026 Sejal Srivastava. All Rights Reserved.
