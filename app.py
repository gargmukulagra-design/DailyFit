import streamlit as st

home = st.Page("Home.py", title="Home", icon="🏠")
profile = st.Page("Profile.py", title="Profile", icon="👤")
meals = st.Page("Meals.py", title="Meals", icon="🍽️")
weight = st.Page("weight.py", title="Weight Tracker", icon="📊")

pg = st.navigation(
    [home, profile, meals, weight]
)

pg.run()
