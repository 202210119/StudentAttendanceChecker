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
            # Check if the username is not already in the list of students for the class
            if st.session_state.username not in st.session_state.classes[class_name]:
                # Assign a new list containing the student's username directly to the 'class_name' key
                st.session_state.classes[class_name] = [st.session_state.username]
                return True
        return False

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
