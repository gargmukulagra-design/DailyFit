import streamlit as st
import sqlite3
from datetime import date
# -----------------------
# DATABASE
# -----------------------

conn = sqlite3.connect(
    "Database.db",
    check_same_thread=False
)

c = conn.cursor()

# -----------------------
# GET USER
# -----------------------

c.execute("""
SELECT *
FROM user_info
LIMIT 1
""")

user = c.fetchone()

# -----------------------
# PAGE
# -----------------------

st.set_page_config(
    page_title="Profile",
    layout="wide"
)
st.title("👤 Profile")

st.divider()

# -----------------------
# NO PROFILE YET
# -----------------------

if user is None:

    st.subheader(
        "Create Your Profile"
    )

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0
    )

    height = st.number_input(
        "Height (cm)",
        min_value=1.0
    )

    if st.button(
        "💾 Save Profile",
        use_container_width=True
    ):

        c.execute("""
        INSERT INTO user_info
        (name,age,sex,weight,height,bmi)
        VALUES(?,?,?,?,?,?)
        """,
        (
            name,
            age,
            sex,
            weight,
            height,
            round(weight/((height/100)**2),2)
        ))

        conn.commit()
        conn.close()

        conn = sqlite3.connect("Database.db")
        c= conn.cursor()

        c.execute("""
        INSERT OR REPLACE INTO weight_history
        VALUES(?,?)
            """,(date.today(),weight))


        conn.commit()
        conn.close()

        st.rerun()

# -----------------------
# PROFILE EXISTS
# -----------------------

else:

    name, age, sex, weight, height,bmi = user

    st.title(
        f"👋 Hello, {name}"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Age", age)

    with c2:
        st.metric("Sex", sex)

    with c3:
        st.metric(
            "Weight",
            f"{weight} kg"
        )

    with c4:
        st.metric(
            "Height",
            f"{height} cm"
        )

    st.write("")

    # -----------------------
    # UPDATE SECTION
    # -----------------------

    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = False

    if not st.session_state.edit_mode:

        if st.button(
            "⚙️ Update Profile",
            use_container_width=True
        ):
            st.session_state.edit_mode = True
            st.rerun()

    else:

        st.subheader(
            "Update Information"
        )

        new_name = st.text_input(
            "Name",
            value=name
        )

        new_age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=age
        )

        new_sex = st.selectbox(
            "Sex",
            ["Male", "Female"],
            index=0 if sex == "Male" else 1
        )

        new_weight = st.number_input(
            "Weight (kg)",
            value=float(weight)
        )

        new_height = st.number_input(
            "Height (cm)",
            value=float(height)
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save Changes",
                use_container_width=True
            ):

                c.execute("""
                UPDATE user_info
                SET
                    name=?,
                    age=?,
                    sex=?,
                    weight=?,
                    height=?,
                    bmi=?
                """,
                (
                    new_name,
                    new_age,
                    new_sex,
                    new_weight,
                    new_height,
                    round(new_weight/((new_height/100)**2),2)
                ))

                conn.commit()

                st.session_state.edit_mode = False

                st.rerun()

        with col2:

            if st.button(
                "❌ Cancel",
                use_container_width=True
            ):

                st.session_state.edit_mode = False

                st.rerun()