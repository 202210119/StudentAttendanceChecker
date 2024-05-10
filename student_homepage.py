import streamlit as st
from authentication import logout
from student import Student
from teacher import Teacher

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        # Get the teacher instance and the teacher's classes
        teacher_instance = Teacher.get_teacher()
        teacher_classes = teacher_instance.get_teacher_classes()

        # Get the student instance
        student_instance = Student.get_student(username)
        if student_instance is not None:
            if student_instance.join_class(class_code, teacher_classes):
                st.success(f"You have joined the class with code '{class_code}'.")
            else:
                st.error("Invalid class code.")

    # Display student's classes
    student_instance = Student.get_student(username)
    if student_instance is not None:
        student_classes = student_instance.get_student_classes()
        st.header("Your Classes")
        if student_classes:
            for class_name in student_classes:
                st.write(class_name)
        else:
            st.write("You haven't joined any classes yet.")

    # Logout button
    if st.button("Logout"):
        logout()
        st.experimental_rerun()
