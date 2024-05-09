import streamlit as st
from authentication import logout
from streamlit_delta_calendar import DeltaCalendar

def student_homepage():
    st.title(f"Welcome, Student {st.session_state.username}!")
    st.write("This is the Student homepage.")

    # Add a calendar for students
    st.write("Student Calendar:")
    calendar = DeltaCalendar()
    calendar
