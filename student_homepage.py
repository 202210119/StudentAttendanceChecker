import streamlit as st
from authentication import logout
from streamlit_calendar import st_calendar

def teacher_homepage():
    st.title(f"Welcome, Teacher {st.session_state.username}!")
    st.write("This is the Teacher homepage.")

    # Add a calendar for teachers
    st.write("Teacher Calendar:")
    date_value = st_calendar(label="Select a date", key="teacher_calendar")
    st.write(f"Selected date: {date_value}")
