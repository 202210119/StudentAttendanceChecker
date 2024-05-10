import streamlit as st
from authentication import logout
from teacher import Teacher
from student import Student
def homepage(username, user_type):
    st.title(f"Welcome, {user_type.capitalize()} {username}!")
    if user_type == "teacher":
        create_teacher_class(username)
    elif user_type == "student":
        join_class(username)
def create_teacher_class(username):
    st.title(f"Welcome, Teacher {username}!")
    st.header("Create a New Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create Class"):
        teacher = Teacher.get_teacher()  # Get the teacher instance
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")
    # Display existing classes
    st.header("Your Classes")
    teacher = Teacher.get_teacher()  # Get the teacher instance
    existing_classes = teacher.get_teacher_classes()  # Removed 'username' argument
    if existing_classes:
        selected_class = st.selectbox("Select Class", [""] + existing_classes)
        if selected_class:
            if st.button("Go to Class"):
                st.session_state.selected_class = selected_class
                st.experimental_rerun()
    else:
        st.info("You haven't created any classes yet.")
def join_class(username):
    st.header("Join a Class")
    st.info("Select a class to join:")
    student = Student.get_student()  # Get the student instance
    existing_classes = student.get_student_classes()  # Use the Student class to get existing classes
    if existing_classes:
        selected_class = st.selectbox("Select Class", [""] + existing_classes)
        if selected_class:
            if st.button("Join Class"):
                if student.join_class(selected_class):
                    st.success(f"You have joined the class '{selected_class}'.")
                    st.session_state.selected_class = selected_class
                else:
                    st.error(f"Failed to join the class '{selected_class}'.")
    else:
        st.info("No classes available to join.")
    if st.button("Logout"):
        logout()
        st.experimental_rerun()
