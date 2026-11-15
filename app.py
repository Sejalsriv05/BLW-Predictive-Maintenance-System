from datetime import datetime, timedelta
import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

model = joblib.load(
    "model/random_forest_model.pkl"
)

st.set_page_config(
    page_title="AI Maintenance Scheduler",
    layout="wide"
)

with st.sidebar:
    st.title("🚂 BLW")
    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🔍 Predictor",
            "📊 Dashboard"
        ]
    )

st.markdown("""
<style>
/* Force Main App and Sidebar to Dark Theme */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #0F172A !important;
}

[data-testid="stSidebar"] {
    background-color: #1E293B !important;
}

/* Force all labels and standard text to be white */
label, label p, p, span {
    color: #F8FAFC !important;
}

/* Keep the text inside info/success warning boxes readable */
div[data-testid="stAlert"] * {
    color: #1E293B !important;
}

h1 {
    color: #38BDF8 !important;
    text-align: center;
}

h2, h3 {
    color: #22C55E !important;
}

div[data-testid="stMetric"] {
    background-color: #1E293B !important;
    border: 1px solid #334155 !important;
    border-radius: 15px !important;
    padding: 15px !important;
}

div[data-testid="stMetric"] * {
    color: #F8FAFC !important;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #22C55E,
        #16A34A
    ) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 10px !important;
    height: 50px !important;
    width: 100% !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True) 

def home_page():
    st.markdown("""
    <div style="
    background: linear-gradient(90deg,#0EA5E9,#2563EB);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
    ">
    <h1>🚂 BLW Predictive Maintenance System</h1>
    <h3>AI-Powered Industrial Maintenance Platform</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Machines Monitored", "250+")
    with col2:
        st.metric("Downtime Reduction", "35%")
    with col3:
        st.metric("Prediction Accuracy", "95%")

    st.markdown("---")
    st.subheader("🎯 System Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✔ Predict Machine Failures")
        st.success("✔ Generate Maintenance Schedule")
        st.success("✔ Health Score Analysis")
    with col2:
        st.success("✔ Failure Risk Detection")
        st.success("✔ Dashboard Analytics")
        st.success("✔ Maintenance Tracking")

    st.markdown("---")
    st.subheader("🏭 About the Project")

    st.info("""
    This AI-powered predictive maintenance platform helps
    Banaras Locomotive Works engineers identify machine
    failures before breakdowns occur.

    The system uses Machine Learning to estimate failure
    probability, calculate health scores, and generate
    optimized maintenance schedules.
    """)

    st.markdown("---")
    st.subheader("🚀 Workflow")

    st.write("""
    1. Enter machine parameters
    2. Run AI prediction
    3. Calculate failure probability
    4. Generate health score
    5. Schedule maintenance automatically
    6. Monitor results through dashboard
    """)


def predictor_page():
    st.markdown("""
    <h1>⚙️ AI-Powered Maintenance Scheduling System</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background: linear-gradient(
    90deg,
    #1E293B,
    #0F172A
    );
    padding:20px;
    border-radius:15px;
    text-align:center;
    margin-bottom:20px;
    ">
    <h2>🚂 Banaras Locomotive Works</h2>
    <p style="color: white !important;">Industrial Predictive Maintenance Platform</p>
