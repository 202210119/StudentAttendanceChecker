import streamlit as st
from authentication import logout
import streamlit_delta_calendar

def student_homepage():
    st.title(f"Welcome, Student {st.session_state.username}!")
    st.write("This is the Student homepage.")

    # Add a calendar for students
    st.write("Student Calendar:")
    calendar = DeltaCalendar()
    calendar
