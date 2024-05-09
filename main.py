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
    page = st.sidebar.radio("Go to", ["Login", "Register"])

    if page == "Login":
        login_page()
    elif page == "Register":
        register_page()

    # Display Teacher or Student homepage if logged in
    if st.session_state.get("logged_in", False):
        if st.session_state.user_type == "teacher":
            teacher_homepage()
        elif st.session_state.user_type == "student":
            student_homepage()

if __name__ == "__main__":
    main()
