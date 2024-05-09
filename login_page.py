import streamlit as st
from authentication import login

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.empty()  # Clear the page
            if st.session_state.user_type == "teacher":
                teacher_homepage(username)
            elif st.session_state.user_type == "student":
                student_homepage(username)