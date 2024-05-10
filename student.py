# student.py
import streamlit as st
from teacher import Teacher

class Student:
    @staticmethod
    def get_student(username):
        if "student" not in st.session_state:
            st.session_state.student = Student()
        return st.session_state.student

    def __init__(self):
        if "classes" not in st.session_state:
            st.session_state.classes = {}

    def join_class(self, class_code, teacher_classes):
        # Check if the class code exists in the teacher's classes
        if class_code in teacher_classes:
            # Initialize the class code list if it doesn't exist
            if class_code not in st.session_state.classes:
                st.session_state.classes[class_code] = []
            # Append the username to the class code list
            st.session_state.classes[class_code].append(st.session_state.username)
            return True
        else:
            return False

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
