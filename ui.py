import streamlit as st

from functions import (
    bmi_category,
    takeinfo
)

def show_ui():

    # PAGE CONFIG
    st.set_page_config(
        page_title="DailyFit",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # TITLE
    st.title("🏋️ DailyFit")

    st.markdown("---")

    # ---------------- SIDEBAR ----------------

    st.sidebar.title("👤 User Profile")

    with st.sidebar.expander(
        "Enter Details",
        expanded=True
    ):

        name = st.text_input("Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100
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

        # BMI
        if height > 0:

            hm = height / 100

            bmi = weight / (hm ** 2)

            category = bmi_category(bmi)

            st.markdown("---")

            st.subheader("BMI Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "BMI",
                    round(bmi, 2)
                )

            with col2:
                st.metric(
                    "Category",
                    category
                )

        # SAVE BUTTON
        if st.sidebar.button(
            "💾 Save Information",
            use_container_width=True
        ):

            takeinfo(
                name,
                age,
                sex,
                weight,
                height
            )

            st.sidebar.success(
                "Information Saved"
            )

    # ---------------- MAIN DASHBOARD ----------------

    st.header("Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            "🍽️ Meal Tracking"
        )

    with col2:

        st.warning(
            "🔥 Activity Tracking"
        )

    with col3:

        st.success(
            "⚖️ Weight Monitoring"
        )

    st.markdown("---")

    # SECOND ROW
    left, right = st.columns([2,1])

    with left:

        st.subheader(
            "Daily Summary"
        )

        st.write(
            "Your reports and analytics will appear here."
        )

    with right:

        st.subheader(
            "Quick Stats"
        )

        st.metric(
            "Calories Intake",
            "0"
        )

        st.metric(
            "Calories Burnt",
            "0"
        )

        st.metric(
            "Net Calories",
            "0"
        )