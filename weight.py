import sqlite3
import streamlit as st
from datetime import date
import pandas as pd
import pickle

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="DailyFit AI Predictor",
    page_icon="🏋️",
    layout="centered"
)

# -----------------------------
# HEADER
# -----------------------------

st.title("🏋️ DailyFit AI Weight Predictor")
st.write("Predict your future weight using your calorie habits and ML model.")
st.divider()

# -----------------------------
# DATABASE
# -----------------------------

day = date.today()

conn = sqlite3.connect(
    "Database.db",
    check_same_thread=False
)

c = conn.cursor()

# -----------------------------
# USER INFO
# -----------------------------

c.execute("SELECT * FROM user_info")

user = c.fetchone()

name, age, sex, weight, height, bmi = user

# -----------------------------
# LAST WEIGHT UPDATE DATE
# -----------------------------

c.execute("""
SELECT * FROM weight_history
ORDER BY date DESC
LIMIT 1
""")

last_date = c.fetchone()[0]

# -----------------------------
# AVG SURPLUS
# -----------------------------

c.execute("""
SELECT AVG(surplus)
FROM summary
WHERE date BETWEEN ? AND ?
""", (last_date, day))

avg_surplus = c.fetchone()[0]

if avg_surplus is None:
    avg_surplus = 0

# -----------------------------
# LOAD MODEL
# -----------------------------

with open("weight_model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------------
# USER DASHBOARD
# -----------------------------

st.subheader(f"Welcome, {name} 👋")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="⚖️ Weight",
        value=f"{weight:.1f} kg"
    )

with col2:
    st.metric(
        label="📊 BMI",
        value=f"{bmi:.1f}"
    )

with col3:
    st.metric(
        label="🔥 Avg Surplus",
        value=f"{avg_surplus:.0f}"
    )

st.divider()

# -----------------------------
# PREDICTION INPUT
# -----------------------------

days = st.number_input(
    "📅 Predict Weight After How Many Days?",
    min_value=1,
    value=30,
    step=1
)

gender = {
    "Male": 0,
    "Female": 1
}

# -----------------------------
# MODEL INPUT
# -----------------------------

input_data = pd.DataFrame(
    [[
        age,
        gender[sex],
        height,
        weight,
        bmi,
        avg_surplus,
        days
    ]],
    columns=[
        "age",
        "sex",
        "height_cm",
        "weight_kg",
        "bmi",
        "avg_surplus",
        "days"
    ]
)

# -----------------------------
# PREDICTION
# -----------------------------

weight_change = model.predict(input_data)[0]

future_weight = weight + weight_change

st.divider()

# -----------------------------
# RESULTS
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📉 Predicted Weight Change",
        f"{weight_change:.2f} kg"
    )

with col2:
    st.metric(
        "🎯 Predicted Weight",
        f"{future_weight:.2f} kg"
    )

st.divider()

# -----------------------------
# INTERPRETATION
# -----------------------------

if weight_change < 0:

    st.success(
        f"🎉 Based on your current calorie habits, "
        f"you may lose approximately "
        f"{abs(weight_change):.2f} kg "
        f"in {int(days)} days."
    )

elif weight_change > 0:

    st.warning(
        f"📈 Based on your current calorie habits, "
        f"you may gain approximately "
        f"{weight_change:.2f} kg "
        f"in {int(days)} days."
    )

else:

    st.info(
        "⚖️ Your weight is expected to remain stable."
    )

# -----------------------------
# FOOTER
# -----------------------------

st.caption(
    "Prediction generated using DailyFit's Machine Learning Model."
)

conn.close()