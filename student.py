# student.py

import streamlit as st

class Student:
    @staticmethod
    def get_student():
        if "student" not in st.session_state:
            st.session_state.student = Student()
        return st.session_state.student

    def __init__(self):
        if "classes" not in st.session_state:
            st.session_state.classes = {}

    def join_class(self, class_name):
        if class_name in st.session_state.classes:
            # Retrieve the list of students for the class, or initialize it as an empty list if it doesn't exist
            students = st.session_state.classes.get(class_name, [])
            # Add the student's username to the list of students for the class
            students.append(st.session_state.username)
            # Update the session state with the modified list of students for the class
            st.session_state.classes[class_name] = students
            return True
        return False

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
