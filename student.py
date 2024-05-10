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
            # If the class already exists, append the student's username to the existing list of students
            st.session_state.classes[class_name].append(st.session_state.username)
        else:
            # If the class doesn't exist, initialize a new list with the student's username
            st.session_state.classes[class_name] = [st.session_state.username]
        return True

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
