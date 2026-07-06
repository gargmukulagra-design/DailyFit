import streamlit as st
from datetime import date
import sqlite3
import pandas as pd
import functions

st.title("DAILY FIT")

c1, c2 = st.columns(2)
with c1:
    st.subheader(f"MEALS")
with c2:
    st.subheader(f"DATE:  {date.today()}")

conn = sqlite3.connect(
    "Database.db",
    check_same_thread=False
)

c = conn.cursor()

c.execute("SELECT * FROM user_info")

user = c.fetchone()

name, age, sex, weight, height, bmi = user

today = str(date.today())

c.execute("""
        SELECT MEAL,CALORIES 
        FROM meal 
        WHERE DATE = ?
        """, (today,))

data = pd.DataFrame(
    c.fetchall(),
    columns=["MEAL", "CALORIES"]
)

st.bar_chart(data, x="MEAL", y="CALORIES")

burnt = functions.burnt_cal(today) or 0
maintenance_cal = 10*weight + 6.25*height - 5*age + burnt + 5

total_Calories_eaten = functions.eaten_cal(today) or 0
calories_required = functions.recommended_calories(maintenance_cal, bmi)

st.write(f"Calories eaten : {total_Calories_eaten}")
st.write(f"Required : {calories_required}")

percentage = (total_Calories_eaten / calories_required) * 100

# Bar settings
bar_width = min(percentage, 100)

if percentage <= 100:
    color = "#28a745"  # Green
else:
    color = "#dc3545"  # Red

# Display stats
st.subheader(f"{total_Calories_eaten} / {calories_required} Calories")
st.write(f"Progress: **{percentage:.1f}%**")

# Custom progress bar
st.markdown(
    f"""
    <div style="
        width:100%;
        background-color:#e9ecef;
        border-radius:10px;
        overflow:hidden;
        margin-top:10px;
        margin-bottom:10px;
    ">
        <div style="
            width:{bar_width}%;
            background-color:{color};
            height:30px;
            text-align:center;
            line-height:30px;
            color:white;
            font-weight:bold;
        ">
            {percentage:.1f}%
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Status message
if percentage < 100:
    remaining = calories_required - total_Calories_eaten
    st.success(f"✅ {remaining} calories remaining")

elif percentage == 100:
    st.success("🎯 Daily calorie goal reached!")

else:
    excess = total_Calories_eaten - calories_required
    st.error(f"⚠️ {excess} calories over target")