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

    def join_classes(self, teacher_classes):
        for class_code in teacher_classes:
            if class_code not in st.session_state.classes:
                st.session_state.classes[class_code] = [st.session_state.username]
            else:
                st.session_state.classes[class_code].append(st.session_state.username)

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
