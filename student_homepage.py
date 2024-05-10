import streamlit as st
from authentication import logout
from student import Student
from teacher import Teacher

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        student_instance = Student.get_student(username)
        if student_instance.join_class(class_code, class_code, Teacher.get_teacher().get_teacher_classes()):
            st.success(f"You have joined the class with code '{class_code}'.")

    if st.button("Logout"):
        logout()
        st.experimental_rerun()
