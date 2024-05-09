import streamlit as st
from login_page import login_page
from register_page import register_page
from teacher_homepage import teacher_homepage
from student_homepage import student_homepage
from initialize import initialize_session_state

def main():
    initialize_session_state()
    
    st.title("Simple Login and Register App")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Register", "Student Homepage", "Teacher Homepage"])

    if page == "Login":
        login_page()
    elif page == "Register":
        register_page()
    elif page == "Student Homepage":
        if st.session_state.logged_in and st.session_state.user_type == "student":
            student_homepage(st.session_state.username)
        else:
            st.warning("You need to login first.")
    elif page == "Teacher Homepage":
        if st.session_state.logged_in and st.session_state.user_type == "teacher":
            teacher_homepage(st.session_state.username)
        else:
            st.warning("You need to login first.")

if __name__ == "__main__":
    main()
