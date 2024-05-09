import streamlit as st
from authentication import logout
import streamlit_delta_calendar

def teacher_homepage():
    st.title(f"Welcome, Teacher {st.session_state.username}!")
    st.write("This is the Teacher homepage.")

    # Add a calendar for teachers
    st.write("Teacher Calendar:")
    calendar = DeltaCalendar()
    calendar
