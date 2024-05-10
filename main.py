# main.py

import streamlit as st
from login_page import login_page
from register_page import register_page
from class_page import class_page
from teacher import Teacher
from homepage import homepage
import initialize 

def main():
    initialize.initialize_session_state()
    
    st.sidebar.title("Navigation")
    pages = ["Login", "Register"]
    if st.session_state.get("logged_in", False):
        if st.session_state.user_type == "teacher":
            pages.append("Teacher Homepage")
            teacher_instance = Teacher.get_teacher()
            for class_name in teacher_instance.get_teacher_classes():
                pages.append(class_name)
        elif st.session_state.user_type == "student":
            pages.append("Student Homepage")

        if "selected_class" in st.session_state:
            pages.append("Class Page")

    page = st.sidebar.radio("Go to", pages)

    if page == "Login":
        login_page()
    elif page == "Register":
        register_page()
    elif page == "Class Page":
        if st.session_state.user_type == "teacher":
            class_page(st.session_state.username, st.session_state.selected_class)
        else:
            class_page(st.session_state.username, page)
    else:
        homepage(st.session_state.username, st.session_state.user_type)

if __name__ == "__main__":
    main()

