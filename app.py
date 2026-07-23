import streamlit as st

from modules import (
    configure_gemini,
    generate_study_plan,
    generate_smart_timetable,
    analyze_subject_priority,
    generate_study_session,
    generate_quiz,
    generate_progress,
    generate_motivation,
    ask_ai,
    study_notifications
)

from utils import load_css


# Page settings
st.set_page_config(
    page_title="AI Study Companion",
    page_icon="📚",
    layout="wide"
)


# Load CSS
st.markdown(load_css("style.css"), unsafe_allow_html=True)


# Title
st.title("📚 AI Powered Study Companion")
st.write("Your personal AI learning assistant")


# Sidebar
st.sidebar.title("⚙️ Settings")


api_key = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password"
)


if api_key:
    model = configure_gemini(api_key)
else:
    model = None



# Student Dashboard

st.sidebar.subheader("👩‍🎓 Student Dashboard")

name = st.sidebar.text_input("Student Name")

student_class = st.sidebar.text_input("Class")

board = st.sidebar.text_input("Board")

percentage = st.sidebar.number_input(
    "Current Percentage",
    min_value=0,
    max_value=100
)

study_hours = st.sidebar.text_input(
    "Daily Study Hours"
)

goal = st.sidebar.text_input(
    "Study Goal"
)

weak_subjects = st.sidebar.text_input(
    "Weak Subjects"
)



# Menu

option = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Study Plan Generator",
        "Smart Timetable",
        "Subject Priority",
        "Study Session",
        "Quiz Generator",
        "Progress Tracker",
        "Motivation",
        "AI Study Assistant"
    ]
)



if model is None:

    st.warning(
        "Please enter your Gemini API Key in the sidebar."
    )


else:


    if option == "Study Plan Generator":

        st.header("📅 Study Plan Generator")

        if st.button("Generate Study Plan"):

            result = generate_study_plan(
                model,
                name,
                student_class,
                board,
                percentage,
                study_hours,
                goal,
                weak_subjects
            )

            st.markdown(result)



    elif option == "Smart Timetable":

        st.header("⏰ Smart Timetable")

        if st.button("Generate Timetable"):

            result = generate_smart_timetable(
                model,
                student_class,
                study_hours,
                weak_subjects
            )

            st.markdown(result)



    elif option == "Subject Priority":

        st.header("📊 Subject Priority Analyzer")

        if st.button("Analyze"):

            result = analyze_subject_priority(
                model,
                percentage,
                weak_subjects,
                goal
            )

            st.write(result)



    elif option == "Study Session":

        st.header("📖 Study Session Planner")

        if st.button("Create Session"):

            result = generate_study_session(
                model,
                study_hours
            )

            st.write(result)



    elif option == "Quiz Generator":

        st.header("📝 AI Quiz Generator")

        subject = st.text_input(
            "Subject"
        )

        if st.button("Generate Quiz"):

            result = generate_quiz(
                model,
                subject,
                student_class
            )

            st.write(result)



    elif option == "Progress Tracker":

        st.header("📈 Progress Tracker")

        completed = st.number_input(
            "Completed Topics",
            min_value=0
        )

        total = st.number_input(
            "Total Topics",
            min_value=1
        )


        if st.button("Check Progress"):

            result = generate_progress(
                model,
                completed,
                total
            )

            st.write(result)

            st.progress(
                int((completed/total)*100)
            )



    elif option == "Motivation":

        st.header("🌟 Motivation Generator")

        if st.button("Generate Motivation"):

            result = generate_motivation(
                model,
                goal
            )

            st.write(result)



    elif option == "AI Study Assistant":

        st.header("🤖 Ask AI")

        question = st.text_input(
            "Ask your study question"
        )


        if st.button("Ask"):

            result = ask_ai(
                model,
                question
            )

            st.write(result)



st.sidebar.info(
    study_notifications()
)
