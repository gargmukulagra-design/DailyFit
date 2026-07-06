import streamlit as st
import sqlite3
import functions
from datetime import date
import time
import variables



profile = st.Page("Profile.py", title="Profile", icon="👤")
meals = st.Page("Meals.py", title="Meals", icon="🍽️")
weight = st.Page("Weight.py", title="Weight Tracker", icon="📊")

pg = st.navigation( [profile, meals, weight])
pg.run()








# today's date
day = str(date.today())

# -----------------------------
# PAGE
# -----------------------------

st.title("DAILY FIT")

st.write(
    "Keeping Track Of Your Daily Goal"
)

st.divider()

# -----------------------------
# DATABASE
# -----------------------------

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

st.header(f"HELLO {name} !")

st.divider()

# -----------------------------
# TOP CARDS
# -----------------------------

c1, c2 = st.columns(2)

# BMI CARD

with c1:

    st.title("📊 BMI")
    st.write(f"WEIGHT : {weight}")
    st.write(f"BMI : {bmi}")

    st.write(
        f"Category : {functions.bmi_category(bmi)}"
    )
#---------------------------UPDATE WEIGHT----------------------------------

if "update_form" not in st.session_state:
    st.session_state.update_form = False

if st.button("UPDATE WEIGHT"):
    st.session_state.update_form = True

if st.session_state.update_form:

    w = st.number_input(
        "ENTER WEIGHT",
        min_value=1.0,
        step=0.1
    )

    if st.button("SAVE WEIGHT(in Kg)"):

        if w > 0:
            conn = sqlite3.connect("Database.db")
            c= conn.cursor()

            c.execute("""
            INSERT OR REPLACE INTO weight_history
            VALUES(?,?)
                """,(day,w))
            
            conn.commit()
            conn.close()

            conn = sqlite3.connect("Database.db")
            c = conn.cursor()
            c.execute("""
    UPDATE user_info
    SET weight = ? , 
    bmi = ?
                """,(w,round(w/((height/100)**2),2)))
            
            conn.commit()
            conn.close()

            st.success(
                "WEIGHT UPDATED SUCCESSFULLY"
            )

            st.session_state.update_form = False
            

            time.sleep(1.5)

            st.rerun()

        else:

            st.warning(
                "ENTER A VALID WEIGHT"
            )

# CALORIES CARD

with c2:

    st.title("CALORIES")
    eaten = functions.eaten_cal(day)
    burnt = functions.burnt_cal(day)

        # if no meals
    if eaten is None:
        eaten = 0

    if burnt is None:
        burnt = 0

    calories = eaten - burnt

#---------------------------------REQUIRED CALORIES-------------------------------
    maintenance_cal= 10*weight + 6.25*height - 5*age + 5 + burnt

    required = functions.recommended_calories(maintenance_cal,bmi)
    st.write(f"Calories    :      {calories}/ {required} ")

    
    surplus = calories - required

    conn = sqlite3.connect("Database.db")
    c = conn.cursor()

    c.execute("""
    INSERT OR REPLACE INTO summary(date, surplus)
    VALUES(?, ?)
    """, (day, surplus))

    conn.commit()

# -----------------------------
# SECOND ROW
# -----------------------------

c3, c4 = st.columns(2)

with c3:
# ------------------- LAST MEAL ---------------------------
    st.title(" Last Meal ")
    c.execute("""
            SELECT * FROM meal
            WHERE DATE = ?
            ORDER BY id DESC
            """,(day,))
    meal = c.fetchone()

    if meal:
        st.write(f"Took On {meal[1]}")
        st.write(f"MEAL : {meal[2]}")
        st.write(f"calories : {meal[3]}")
    else:
        st.write("No Meal added today")

#----------------- ADD MEAL ---------------------------------
    if "show_meal_form" not in st.session_state:
        st.session_state.show_meal_form = False


    if st.button("Add Meal"):
        st.session_state.show_meal_form = True

    if st.session_state.show_meal_form:

        M = st.text_input("Meal:")
        C = st.text_input("Calories:")

        if st.button("Save Meal"):

            if M and C:

                functions.AddMeal(M, C)

                st.success("Meal Added Successfully")

                st.session_state.show_meal_form = False
                time.sleep(1.5)
                st.rerun()

            else:
                st.warning("Fill all fields")




with c4:
#-------------------------- LAST ACTIVITY -----------------------
    st.title(" last Activity ")
    c.execute("""
            SELECT * FROM activity
            WHERE date = ?
            ORDER BY id DESC
            """,(day,))
    activity = c.fetchone()

    if activity:
        st.write(f"Took On {activity[1]}")
        st.write(f"ACTIVITY : {activity[2]}")
        st.write(f"Calories Burnt : {activity[3]}")
    else:
        st.write("No Activity Done")

#---------------------------- ADD ACTIVITY --------------------------
    if "add_activity" not in st.session_state:
        st.session_state.add_activity = False

    if st.button("Add A Activity"):
        st.session_state.add_activity = True

    if st.session_state.add_activity:
         t = st.text_input("Enter Activity")
         cal = st.text_input("Calories Burnt")

         if st.button("Save Activity"):
            if t and cal:
                functions.AddActivity(t,cal)
                st.success("Activity Added")
                st.session_state.add_activity = False
                st.rerun()
            else:
                st.warning("Fill All Fields")

#-------------------------------- reuired calories --------------------------