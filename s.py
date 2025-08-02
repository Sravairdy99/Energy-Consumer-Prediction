import pandas as pd
import streamlit as st
import joblib
import datetime

# Load model
model = joblib.load("RandomForestModel.pkl")

# Page config
st.set_page_config(page_title="Smart Home Energy Estimator", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background-image: url('https://cdn.wallpapersafari.com/49/28/PFEVOY.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #000;
    }

    /* Global text styling */
    h1, h2, h3, h4, h5, h6, p, label, div {
        color: #000 !important;
        font-weight: bold !important;
    }

    /* Input styling */
    .stNumberInput, .stSelectbox, .stTextInput, .stCheckbox, .stRadio {
        background-color: rgba(255, 255, 255, 0.85) !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Button Styling - White Button */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 10px;
        font-weight: bold;
        border: 1px solid #000;
        padding: 10px 20px;
    }

    /* Metric container */
    div[data-testid="metric-container"] {
        background-color: rgba(255,255,255,0.8);
        border-radius: 10px;
        border: 1px solid #00000022;
        padding: 10px;
        text-align: center;
    }
    div[data-testid="metric-container"] h1 {
        color: #000 !important;
    }

    /* Success message styling */
    div.stAlert {
        background-color: rgba(255, 255, 255, 0.85) !important;
        border-left: 6px solid green;
        border-radius: 10px;
        color: #000 !important;
        font-weight: bold;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 6px;
        color: #000 !important;
        font-weight: bold;
        padding: 6px;
    }

    /* DataFrame style */
    .stDataFrameContainer {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("🌿 Smart Home Energy Consumption Estimator")
st.markdown("Efficient homes save energy and the planet 🌍.")
st.markdown("Enter your details to estimate usage.")
st.markdown("---")
st.subheader("🏡 Home Details")

# ---------- Inputs ----------
col1, col2, col3 = st.columns(3)

with col1:
    num_occupants = st.number_input("👨‍👩‍👧‍👦 Number of Occupants", min_value=1, value=3)
    year = st.number_input("📅 Year", min_value=2000, max_value=2035, value=2025)
    day = st.number_input("📆 Day", min_value=1, max_value=31, value=1)
    heating_type = st.selectbox("🔥 Heating Type", ["Electric", "Gas", "None"])

with col2:
    house_size_sqft = st.number_input("🏠 House Size (sqft)", min_value=100, value=1500)
    month = st.number_input("🗓️ Month", min_value=1, max_value=12, value=8)
    outside_temp_celsius = st.number_input("🌡️ Outdoor Temp (°C)", min_value=10, max_value=45, value=27)
    cooling_type = st.selectbox("❄️ Cooling Type", ["Ac", "Fan", "None"])

with col3:
    monthly_income = st.number_input("💰 Monthly Income (₹)", min_value=500, value=25000)
    manual_override = st.radio("🛠️ Manual Override Active?", ["Y", "N"])
    energy_star_home = st.checkbox("✅ Certified Energy Star Home", value=False)

# ---------- Feature Engineering ----------
obj = datetime.date(year, month, day)
day_of_week = obj.weekday()

season_label = (
    "winter" if month in [12, 1, 2] else
    "summer" if month in [3, 4, 5] else
    "fall" if month in [6, 7, 8] else
    "spring"
)

is_weekend = int(day_of_week >= 5)
temp_above_avg = int(outside_temp_celsius > 28)
income_per_person = monthly_income / num_occupants
square_feet_per_person = house_size_sqft / num_occupants
high_income_flag = int(monthly_income > 40000)
low_temp_flag = int(outside_temp_celsius < 28)

features = {
    'num_occupants': num_occupants,
    'house_size_sqft': house_size_sqft,
    'monthly_income': monthly_income,
    'outside_temp_celsius': outside_temp_celsius,
    'year': year,
    'month': month,
    'day': day,
    'heating_type_Electric': int(heating_type == "Electric"),
    'heating_type_Gas': int(heating_type == "Gas"),
    'heating_type_None': int(heating_type == "None"),
    'cooling_type_AC': int(cooling_type == "Ac"),
    'cooling_type_Fan': int(cooling_type == "Fan"),
    'cooling_type_None': int(cooling_type == "None"),
    'manual_override_Y': int(manual_override == "Y"),
    'manual_override_N': int(manual_override == "N"),
    'is_weekend': is_weekend,
    'temp_above_avg': temp_above_avg,
    'income_per_person': income_per_person,
    'square_feet_per_person': square_feet_per_person,
    'high_income_flag': high_income_flag,
    'low_temp_flag': low_temp_flag,
    'season_spring': int(season_label == 'spring'),
    'season_summer': int(season_label == 'summer'),
    'season_fall': int(season_label == 'fall'),
    'season_winter': int(season_label == 'winter'),
    'day_of_week_0': int(day_of_week == 0),
    'day_of_week_6': int(day_of_week == 6),
    'energy_star_home': int(energy_star_home)
}

input_df = pd.DataFrame([features])

# ---------- Prediction Section ----------
st.markdown("---")
st.subheader("⚡ Estimate Your Monthly Energy Usage")

if st.button("🔍 Predict Now"):
    prediction = model.predict(input_df)[0]

    st.markdown("""
        <div style="
            background-color: #d0eaff;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin: 40px auto;
            width: 70%;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        ">
            <h2 style="color:#000;">⚡ Estimate Your Monthly Energy Usage</h2>
            <h1 style="font-size: 48px; color: #003366;">🔋 {0:.2f} kWh</h1>
            <p style="font-size: 20px; color: #000;">✅ Done! Your home’s estimated energy usage is shown above.</p>
        </div>
    """.format(prediction), unsafe_allow_html=True)

    with st.expander("📦 Input Summary"):
        st.dataframe(input_df.T.rename(columns={0: "Value"}))
