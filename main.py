# main.py
import streamlit as st
from login_page import login_page
from register_page import register_page
from teacher_homepage import teacher_homepage
from student_homepage import student_homepage
from class_page import class_page
from initialize import initialize_session_state
from teacher import Teacher

def main():
    initialize_session_state()
    
    st.sidebar.title("Navigation")
    pages = ["Login", "Register"]
    if st.session_state.get("logged_in", False):
        if st.session_state.user_type == "teacher":
            pages.extend(["Teacher Homepage"])
            teacher = Teacher.get_teacher()
            for class_name in teacher.get_teacher_classes():
                pages.append(class_name)
            pages.append("Create Class")
        elif st.session_state.user_type == "student":
            pages.append("Student Homepage")

        if "selected_class" in st.session_state:
            pages.append("Class Page")

    page = st.sidebar.radio("Go to", pages)

    if page == "Login":
        login_page()
    elif page == "Register":
        register_page()
    elif page == "Teacher Homepage":
        teacher_homepage(st.session_state.username)
    elif page == "Student Homepage":
        student_homepage(st.session_state.username)
    elif page == "Create Class":
        # Show the create class page
        create_class_page()
    elif page == "Class Page":
        class_page(st.session_state.username, st.session_state.selected_class)
    else:
        if page in teacher.get_teacher_classes():
            class_page(st.session_state.username, page)

if __name__ == "__main__":
    main()
