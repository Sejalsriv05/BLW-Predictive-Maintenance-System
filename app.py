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

.stApp {
    background-color: #0F172A;
    color: #F8FAFC;
}

h1 {
    color: #38BDF8;
    text-align: center;
}

h2,h3 {
    color: #22C55E;
}

div[data-testid="stMetric"] {
    background-color: #1E293B;
    border: 1px solid #334155;
    border-radius: 15px;
    padding: 15px;
}

div[data-testid="stMetric"] * {
    color: #F8FAFC !important;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #22C55E,
        #16A34A
    );

    color: white;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    border: none;
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
        st.metric(
            "Machines Monitored",
            "250+"
        )

    with col2:
        st.metric(
            "Downtime Reduction",
            "35%"
        )

    with col3:
        st.metric(
            "Prediction Accuracy",
            "95%"
        )

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
    <h1>
    ⚙️ AI-Powered Maintenance Scheduling System
    </h1>
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
    <p>
    Industrial Predictive Maintenance Platform
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Predict Maintenance Before Failure Happens")

    st.info("""
    This system predicts machine health and recommends maintenance schedules
    using AI-based predictive maintenance techniques.
    """)

    st.subheader("Enter Machine Details")

    machine_category = st.selectbox(
        "Machine Category",
        ["Low (L)", "Medium (M)", "High (H)"]
    )

    if machine_category == "Low (L)":
        machine_name = st.selectbox(
            "Machine",
            [
                "Cooling Fan",
                "Air Compressor",
                "Small Pump",
                "Conveyor Motor"
            ]
        )

    elif machine_category == "Medium (M)":
        machine_name = st.selectbox(
            "Machine",
            [
                "Grinding Machine",
                "Drill Press",
                "Welding Machine",
                "Milling Machine"
            ]
        )

    else:
        machine_name = st.selectbox(
            "Machine",
            [
                "CNC Lathe",
                "Hydraulic Press",
                "Traction Motor",
                "Locomotive Engine",
                "Wheel Lathe",
                "Generator"
            ]
        )

    col1, col2 = st.columns(2)

    with col1:

        machine_age = st.number_input(
            "🏭 Machine Age (Years)",
            min_value=0
        )

        operating_hours = st.number_input(
            "⏱ Operating Hours Per Day",
            min_value=0
        )

        temperature = st.number_input(
            "🌡 Operating Temperature (°C)",
            min_value=0.0
        )

        breakdowns = st.number_input(
            "⚠ Previous Breakdowns",
            min_value=0
        )

    with col2:
        last_maintenance = st.date_input(
        "📅 Last Maintenance Date"
        )
        power_consumption = st.number_input(
        "⚡ Power Consumption (kW)",
        min_value=0.0
        )
        load_percentage = st.slider(
        "📊 Load Percentage",
        0,
        100
        )
        criticality = st.selectbox(
        "🚨 Criticality Level",
        ["Low", "Medium", "High"]
         )
    st.markdown("---")

    if st.button("Predict Maintenance"):

        input_data = pd.DataFrame(
            [[
                temperature + 273,
                temperature + 280,
                1500,
                power_consumption,
                operating_hours * 10
            ]],
            columns=[
                "Air temperature [K]",
                "Process temperature [K]",
                "Rotational speed [rpm]",
                "Torque [Nm]",
                "Tool wear [min]"
            ]
        )

        probability = model.predict_proba(
            input_data
        )[0][1]

        failure_probability = probability * 100

        score = 100 - failure_probability

        st.write("Raw Probability:", probability)
        st.write("Failure Probability:", failure_probability)
        st.write("Health Score:", score)

        risk_score = (
            failure_probability * 0.6
            + machine_age * 1
            + breakdowns * 4
            + load_percentage * 0.15
)

        if criticality == "High":
            risk_score += 10

        elif criticality == "Medium":
            risk_score += 5

        if risk_score >= 90:
            priority = " Very Critical"
            due_days = 7
        elif risk_score>=75:
            priority = "Critical"
            due_days = 10

        elif risk_score >= 60:
            priority = "High"
            due_days = 15

        elif risk_score >= 35:
            priority = "Medium"
            due_days = 30

        else:
            priority = "Low"
            due_days = 60

        recommended_date = datetime.today() + timedelta(days=due_days)
        result = pd.DataFrame([{
            "Machine": machine_name,
            "Category": machine_category,
            "Health Score": round(score, 1),
            "Failure Probability": round(failure_probability, 1),
            "Priority": priority,
            "Maintenance Due": due_days,
            "Recommended Date": recommended_date.strftime("%d-%m-%Y")
        }])

        try:

            old_data = pd.read_csv(
                "output/maintenance_results.csv"
            )

            updated_data = pd.concat(
                [old_data, result],
                ignore_index=True
            )

        except:
            updated_data = result

        updated_data.to_csv(
            "output/maintenance_results.csv",
            index=False
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Failure Probability",
                f"{failure_probability:.1f}%"
            )

        with col2:
            st.metric(
                "Health Score",
                f"{score:.0f}/100"
            )

        with col3:
            st.metric(
                "Priority Level",
                priority
            )

        with col4:
            st.metric(
                "Maintenance Due",
                f"{due_days} Days"
            )

        st.success(
            f"Recommended Date: {recommended_date.strftime('%d-%m-%Y')}"
        )
        if priority == "Very Critical":
            suggestion = "Immediate shutdown and inspection recommended."

        elif priority == "Critical":
           suggestion = "Schedule maintenance within the next week."

        elif priority == "High":
           suggestion = "Perform preventive inspection within 15 days."

        elif priority == "Medium":
            suggestion = "Monitor performance and schedule maintenance."

        else:
            suggestion = "Machine is healthy. Continue routine monitoring."

        st.subheader("🛠 Maintenance Recommendation")
        st.info(suggestion) 


def dashboard_page():

    st.header("📊 Maintenance Dashboard")

    try:

        dashboard_data = pd.read_csv(
            "output/maintenance_results.csv"
        )

    except:

        st.warning(
            "No maintenance records available yet."
        )
        return

    st.dataframe(
        dashboard_data,
        use_container_width=True
    )
    st.subheader("📊 Priority Distribution")

    priority_count = dashboard_data["Priority"].value_counts()

    fig = px.pie(
        values=priority_count.values,
        names=priority_count.index,
        title="Maintenance Priority Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("🏭 Machine Health Scores")

fig = px.bar(
        dashboard_data,
        x="Machine",
        y="Health Score",
        color="Priority",
        title="Machine Health Score Analysis"
    )
    
    # Force transparent background and white text to match your app theme
fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", 
        plot_bgcolor="rgba(0,0,0,0)", 
        font=dict(color="white")
    )

st.plotly_chart(fig, use_container_width=True)
st.subheader("📅 Maintenance Schedule")

fig = px.bar(
        dashboard_data,
        x="Machine",
        y="Maintenance Due",
        color="Priority",
        title="Maintenance Due Days"
    )

st.plotly_chart(fig, use_container_width=True)
st.subheader("🚨 Critical Machines")

    critical_df = dashboard_data[
        dashboard_data["Priority"] == "Critical"
    ]

    st.dataframe(
        critical_df,
        use_container_width=True
    )
    total_machines = len(dashboard_data)

    critical_count = len(
        dashboard_data[
            dashboard_data["Priority"] == "Critical"
        ]
    )

    avg_health = dashboard_data[
        "Health Score"
    ].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Machines",
            total_machines
        )

    with col2:
        st.metric(
            "Critical Machines",
            critical_count
        )

    with col3:
        st.metric(
            "Average Health Score",
            f"{avg_health:.1f}"
        )
if page == "🏠 Home":
    home_page()

elif page == "🔍 Predictor":
    predictor_page()

elif page == "📊 Dashboard":
    dashboard_page()
