# student_homepage.py
import streamlit as st
from authentication import logout
from student import Student
from teacher import Teacher

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        student = Student.get_student(username)
        teacher_instance = Teacher.get_teacher()
        if student.join_class(class_code, teacher_instance.get_teacher_classes()):
            st.success(f"You have joined the class with code '{class_code}'.")

    student_instance = Student.get_student(username)
    if student_instance is not None:  # Check if student_instance is not None
        student_classes = student_instance.get_student_classes()
        st.header("Your Classes")
        if student_classes:
            for class_name in student_classes:
                st.write(class_name)
        else:
            st.write("You haven't joined any classes yet.")

    if st.button("Logout"):
        logout()
        st.experimental_rerun()