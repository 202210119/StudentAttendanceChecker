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
    pages = ["Login", "Register"]
    if st.session_state.get("logged_in", False):
        # Add user-specific homepage to navigation
        if st.session_state.user_type == "teacher":
            pages.append("Teacher Homepage")
        elif st.session_state.user_type == "student":
            pages.append("Student Homepage")

    page = st.sidebar.radio("Go to", pages)

    if page == "Login":
        login_page()
    elif page == "Register":
        register_page()
    elif page == "Teacher Homepage":
        teacher_homepage()
    elif page == "Student Homepage":
        student_homepage()

if __name__ == "__main__":
    main()
