# authentication.py

import streamlit as st
from initialize import initialize_session_state

def register_teacher(username, password):
    initialize_session_state()  # Ensure session state is initialized
    if username in st.session_state.teacher_users:
        st.warning("Teacher account already exists! Please choose a different username.")
        return False
    elif username in st.session_state.student_users:
        st.warning("An account with this username already exists as a student! Please choose a different username.")
        return False
    else:
        st.session_state.teacher_users[username] = password
        st.success("Teacher account registration successful! You can now login.")
        return True

def register_student(username, password):
    initialize_session_state()
    if username in st.session_state.student_users:
        st.warning("Student account already exists! Please choose a different username.")
        return False
    elif username in st.session_state.teacher_users:
        st.warning("An account with this username already exists as a teacher! Please choose a different username.")
        return False
    else:
        st.session_state.student_users[username] = password
        st.success("Student account registration successful! You can now login.")
        return True

def login(username, password):
    if username in st.session_state.teacher_users and st.session_state.teacher_users[username] == password:
        st.session_state.logged_in = True
        st.session_state.user_type = "teacher"
        st.session_state.username = username
        return True
    elif username in st.session_state.student_users and st.session_state.student_users[username] == password:
        st.session_state.logged_in = True
        st.session_state.user_type = "student"
        st.session_state.username = username
        return True
    else:
        st.error("Invalid username or password. Please try again.")
        return False

def logout():
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.username = None
