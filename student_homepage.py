import streamlit as st
from authentication import logout
from streamlit_calendar import st_calendar

def student_homepage():
    st.title(f"Welcome, Student {st.session_state.username}!")
    st.write("This is the Student homepage.")

    # Add a calendar for students
    st.write("Student Calendar:")
    date_value = st_calendar(label="Select a date", key="student_calendar")
    st.write(f"Selected date: {date_value}")
