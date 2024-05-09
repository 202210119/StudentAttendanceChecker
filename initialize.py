import streamlit as st

def initialize_session_state():
    if "teacher_users" not in st.session_state:
        st.session_state.teacher_users = {}
    if "student_users" not in st.session_state:
        st.session_state.student_users = {}
