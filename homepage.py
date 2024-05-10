# homepage.py
import streamlit as st
from teacher import Teacher
from student import Student

def homepage(username, user_type):
    st.title(f"Welcome, {user_type.capitalize()} {username}!")

    if user_type == "teacher":
        teacher_homepage(username)
    elif user_type == "student":
        student_homepage(username)

def teacher_homepage(username):
    st.header("Create a New Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create Class"):
        teacher = Teacher.get_teacher()
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

    st.header("Your Classes")
    teacher_instance = Teacher.get_teacher()
    existing_classes = teacher_instance.get_teacher_classes()
    if existing_classes:
        selected_class = st.selectbox("Select Class", [""] + existing_classes)
        if selected_class:
            if st.button("Go to Class"):
                st.session_state.selected_class = selected_class
                st.experimental_rerun()  # Reload the app to go to the selected class
    else:
        st.info("You haven't created any classes yet.")

def student_homepage(username):
    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        student = Student.get_student(username)
        teacher_instance = Teacher.get_teacher()
        if student.join_class(class_code, teacher_instance.get_teacher_classes()):
            st.success(f"You have joined the class with code '{class_code}'.")
            st.session_state.selected_class = class_code
            st.experimental_rerun()  # Reload the app to go to the selected class

    st.header("Your Classes")
    student_instance = Student.get_student(username)
    student_classes = student_instance.get_student_classes()
    if student_classes:
        selected_class = st.selectbox("Select Class", [""] + student_classes)
        if selected_class:
            if st.button("Go to Class"):
                st.session_state.selected_class = selected_class
                st.experimental_rerun()  # Reload the app to go to the selected class
    else:
        st.info("You haven't joined any classes yet.")
