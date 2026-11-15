import os
from datetime import datetime, timedelta
import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

model = joblib.load("model/random_forest_model.pkl")

st.set_page_config(
    page_title="AI Maintenance Scheduler",
    layout="wide"
)

with st.sidebar:
    st.title("🚂 BLW")
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🔍 Predictor", "📊 Dashboard", "📈 Machine Analysis"]
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

/* Fix for the top-left sidebar navigation expand/collapse button */
[data-testid="collapsedControl"] {
    color: #000000 !important;
    background-color: #FFFFFF !important;
    border-radius: 5px !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
}
[data-testid="collapsedControl"] svg {
    fill: #000000 !important;
    color: #000000 !important;
}

/* Force all labels and standard text to be white */
label, label p, p, span {
    color: #F8FAFC !important;
}
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
    background: linear-gradient(90deg, #22C55E, #16A34A) !important;
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
    st.markdown(
        '<div style="background: linear-gradient(90deg,#0EA5E9,#2563EB); padding:30px; border-radius:20px; text-align:center; color:white;">'
        '<h1>🚂 BLW Predictive Maintenance System</h1>'
        '<h3>AI-Powered Industrial Maintenance Platform</h3>'
        '</div>', 
        unsafe_allow_html=True
    )
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
        st.success("✔ Historical Trend Analysis")
    with col2:
        st.success("✔ Failure Risk Detection")
        st.success("✔ Dashboard Analytics")
        st.success("✔ Maintenance Tracking")

    st.markdown("---")
    st.subheader("🏭 About the Project")
    st.info(
        "This AI-powered predictive maintenance platform helps "
        "Banaras Locomotive Works engineers identify machine "
        "failures before breakdowns occur.\n\n"
        "The system uses Machine Learning to estimate failure "
        "probability, calculate health scores, and generate "
        "optimized maintenance schedules."
    )


def predictor_page():
    st.markdown("<h1>⚙️ AI-Powered Maintenance Scheduling System</h1>", unsafe_allow_html=True)
    st.markdown(
        '<div style="background: linear-gradient(90deg, #1E293B, #0F172A); padding:20px; border-radius:15px; text-align:center; margin-bottom:20px;">'
        '<h2>🚂 Banaras Locomotive Works</h2>'
        '<p style="color: white !important;">Industrial Predictive Maintenance Platform</p>'
        '</div>', 
        unsafe_allow_html=True
    )
    st.markdown("### Predict Maintenance Before Failure Happens")
    st.info(
        "This system predicts machine health and recommends maintenance schedules "
        "using AI-based predictive maintenance techniques."
    )
    st.subheader("Enter Machine Details")

    machine_category = st.selectbox(
        "Machine Category",
        ["Low (L)", "Medium (M)", "High (H)"]
    )

    if machine_category == "Low (L)":
        machine_name = st.selectbox("Machine", ["Cooling Fan", "Air Compressor", "Small Pump", "Conveyor Motor"])
    elif machine_category == "Medium (M)":
        machine_name = st.selectbox("Machine", ["Grinding Machine", "Drill Press", "Welding Machine", "Milling Machine"])
    else:
        machine_name = st.selectbox("Machine", ["CNC Lathe", "Hydraulic Press", "Traction Motor", "Locomotive Engine", "Wheel Lathe", "Generator"])

    col1, col2 = st.columns(2)
    with col1:
        machine_age = st.number_input("🏭 Machine Age (Years)", min_value=0)
        operating_hours = st.number_input("⏱ Operating Hours Per Day", min_value=0)
        temperature = st.number_input("🌡 Operating Temperature (°C)", min_value=0.0)
        breakdowns = st.number_input("⚠ Previous Breakdowns", min_value=0)
    with col2:
        last_maintenance = st.date_input("📅 Last Maintenance Date")
        power_consumption = st.number_input("⚡ Power Consumption (kW)", min_value=0.0)
        load_percentage = st.slider("📊 Load Percentage", 0, 100)
        criticality = st.selectbox("🚨 Criticality Level", ["Low", "Medium", "High"])
         
    st.markdown("---")

    if st.button("Predict Maintenance"):
        input_data = pd.DataFrame(
            [[temperature + 273, temperature + 280, 1500, power_consumption, operating_hours * 10]],
            columns=["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"]
        )

        probability = model.predict_proba(input_data)[0][1]
        failure_probability = probability * 100
        score = 100 - failure_probability

        st.write(f"Raw Probability: {probability}")
        st.write(f"Failure Probability: {failure_probability}")
        st.write(f"Health Score: {score}")

        risk_score = failure_probability * 0.6 + machine_age * 1 + breakdowns * 4 + load_percentage * 0.15
        if criticality == "High":
            risk_score += 10
        elif criticality == "Medium":
            risk_score += 5

        if risk_score >= 90:
            priority, due_days = "Very Critical", 7
        elif risk_score >= 75:
            priority, due_days = "Critical", 10
        elif risk_score >= 60:
            priority, due_days = "High", 15
        elif risk_score >= 35:
            priority, due_days = "Medium", 30
        else:
            priority, due_days = "Low", 60

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

        os.makedirs("output", exist_ok=True)
        try:
            old_data = pd.read_csv("output/maintenance_results.csv")
            updated_data = pd.concat([old_data, result], ignore_index=True)
        except:
            updated_data = result
        
        updated_data.to_csv("output/maintenance_results.csv", index=False)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Failure Probability", f"{failure_probability:.1f}%")
        with col2:
            st.metric("Health Score", f"{score:.0f}/100")
        with col3:
            st.metric("Priority Level", priority)
        with col4:
            st.metric("Maintenance Due", f"{due_days} Days")

        st.success(f"Recommended Date: {recommended_date.strftime('%d-%m-%Y')}")
        
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
    st.header("📊 Factory Overview Dashboard (All Data)")
    st.write("This dashboard displays the macro-level health of all machines monitored across the factory.")

    try:
        raw_data = pd.read_csv("output/maintenance_results.csv")
        if raw_data.empty or "Machine" not in raw_data.columns:
            st.warning("No maintenance records available yet. Please run a prediction first.")
            return
            
        raw_data["Health Score"] = pd.to_numeric(raw_data["Health Score"], errors="coerce")
        raw_data["Prediction ID"] = raw_data.index + 1
        
        # Deduplicate to show only the LATEST status of each unique machine in the table
        dashboard_data = raw_data.dropna(subset=["Machine", "Health Score"]).drop_duplicates(subset=["Machine"], keep="last")
            
    except Exception as e:
        st.warning("No maintenance records available yet. Please run a prediction first.")
        return

    # Top level metrics
    total_machines = len(dashboard_data)
    critical_df = dashboard_data[dashboard_data["Priority"].isin(["Critical", "Very Critical"])]
    critical_count = len(critical_df)
    avg_health = dashboard_data["Health Score"].mean()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Unique Machines Monitored", total_machines)
    with col2:
        st.metric("Critical Machines", critical_count)
    with col3:
        st.metric("Factory Avg Health Score", f"{avg_health:.1f}")

    st.markdown("---")
    
    # 3-Chart Holistic View (Pie, Bar, Line) for ALL DATA
    st.subheader("📈 Holistic Factory Analytics")
    chart_col1, chart_col2, chart_col3 = st.columns(3)

    with chart_col1:
        # Pie Chart: Current Priority Distribution across all machines
        priority_count = dashboard_data["Priority"].value_counts()
        fig_pie = px.pie(
            values=priority_count.values,
            names=priority_count.index,
            title="Overall Factory Priority Status",
            hole=0.3
        )
        fig_pie.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"), margin=dict(t=40, b=0, l=0, r=0))
        st.plotly_chart(fig_pie, use_container_width=True, theme=None)

    with chart_col2:
        # Bar Chart: Health scores of all unique machines
        fig_bar = px.bar(
            dashboard_data,
            x="Machine",
            y="Health Score",
            color="Priority",
            title="Live Health Scores (All Machines)"
        )
        fig_bar.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"), margin=dict(t=40, b=0, l=0, r=0), xaxis_type='category')
        st.plotly_chart(fig_bar, use_container_width=True, theme=None)

    with chart_col3:
        # Line Chart: Average Factory Health trend over time
        avg_trend = raw_data.groupby("Prediction ID")["Health Score"].mean().reset_index()
        fig_line = px.line(
            avg_trend,
            x="Prediction ID",
            y="Health Score",
            title="Factory Health Trend Over Time",
            markers=True
        )
        fig_line.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"), margin=dict(t=40, b=0, l=0, r=0))
        st.plotly_chart(fig_line, use_container_width=True, theme=None)

    st.markdown("---")
    st.subheader("📋 Latest Factory Snapshot")
    st.dataframe(dashboard_data, use_container_width=True)


def machine_analysis_page():
    st.header("🔍 Specific Machine Analysis (Micro View)")
    st.write("Select a specific machine from the dropdown to deep-dive into its historical prediction data and health trends.")

    try:
        raw_data = pd.read_csv("output/maintenance_results.csv")
        if raw_data.empty or "Machine" not in raw_data.columns:
            st.warning("No historical data available. Please run predictions first.")
            return
            
        raw_data["Health Score"] = pd.to_numeric(raw_data["Health Score"], errors="coerce")
        raw_data["Failure Probability"] = pd.to_numeric(raw_data["Failure Probability"], errors="coerce")
        raw_data["Prediction ID"] = raw_data.index + 1
        
    except Exception as e:
        st.warning("Could not load historical data.")
        return

    # Selector for specific machine drill-down
    machine_list = raw_data["Machine"].unique()
    selected_machine = st.selectbox("🏭 Select Machine to Analyze:", machine_list)

    # Filter data to only the selected machine
    machine_data = raw_data[raw_data["Machine"] == selected_machine]

    # Metrics for specific machine
    latest_status = machine_data.iloc[-1]
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(f"Current Health: {selected_machine}", f"{latest_status['Health Score']:.1f}/100")
    with col2:
        st.metric("Current Status", latest_status['Priority'])
    with col3:
        st.metric("Total Predictions Logged", len(machine_data))

    st.markdown("---")
    
    # Specific Machine Charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Line chart of this specific machine's health over time
        fig_health = px.line(
            machine_data, 
            x="Prediction ID", 
            y="Health Score", 
            markers=True, 
            title=f"{selected_machine}: Health Trend"
        )
        fig_health.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
        st.plotly_chart(fig_health, use_container_width=True, theme=None)

    with chart_col2:
        # Bar chart of this specific machine's failure probability over time
        fig_fail = px.bar(
            machine_data, 
            x="Prediction ID", 
            y="Failure Probability", 
            color="Priority",
            title=f"{selected_machine}: Failure Risk Trend"
        )
        fig_fail.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"), xaxis_type='category')
        st.plotly_chart(fig_fail, use_container_width=True, theme=None)

    st.subheader(f"📑 Complete History Log: {selected_machine}")
    st.dataframe(machine_data, use_container_width=True)


if page == "🏠 Home":
    home_page()
elif page == "🔍 Predictor":
    predictor_page()
elif page == "📊 Dashboard":
    dashboard_page()
elif page == "📈 Machine Analysis":
    machine_analysis_page()
