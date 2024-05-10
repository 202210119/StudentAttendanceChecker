import streamlit as st
from login_page import login_page
from register_page import register_page
from teacher_homepage import teacher_homepage
from student_homepage import student_homepage
from class_page import class_page
from teacher import Teacher
import initialize 
def main():
    initialize.initialize_session_state()
    
    st.title("Simple Login and Register App")

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
    elif page == "Teacher Homepage":
        teacher_homepage(st.session_state.username)
    elif page == "Student Homepage":
        student_homepage(st.session_state.username)
    elif page == "Class Page":
        class_page(st.session_state.username, st.session_state.selected_class)
    else:
        if page in teacher_instance.get_teacher_classes():
            class_page(st.session_state.username, page)

if __name__ == "__main__":
    main()
