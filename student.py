# student.py
import streamlit as st

class Student:
    @staticmethod
    def get_student(username):
        if "students" not in st.session_state:
            st.session_state.students = {}
        if username not in st.session_state.students:
            st.session_state.students[username] = Student()
        return st.session_state.students[username]

    def __init__(self):
        if "classes" not in st.session_state:
            st.session_state.classes = {}

    def join_class(self, class_name, teacher_classes):
        if class_name in teacher_classes:
            if class_name not in st.session_state.classes:
                st.session_state.classes[class_name] = []
            st.session_state.classes[class_name].append(self)
            return True
        else:
            return False

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
