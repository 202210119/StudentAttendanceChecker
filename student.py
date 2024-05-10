# student.py
import streamlit as st
from teacher import Teacher  # Import the Teacher class directly from Teacher.py

class Student:
    @staticmethod
    def get_student(username):
        if username not in st.session_state:
            st.session_state[username] = Student(username)
        return st.session_state[username]

    def __init__(self, username):
        self.username = username

    def join_class(self, class_name, class_code, teacher_classes):
        if class_code in teacher_classes:
            if class_name not in teacher_classes[class_code]:
                teacher_classes[class_code].append(class_name)
                return True 
        return False
