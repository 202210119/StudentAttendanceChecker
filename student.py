import streamlit as st
from authentication import logout
from teacher import Teacher  # Import the Teacher class

class Student:
    @staticmethod
    def get_student(username):
        # Check if "student" key exists in session_state and return None if it doesn't
        if "student" not in st.session_state:
            return None
        return st.session_state.student

    def __init__(self, username):
        self.username = username

    def join_class(self, class_code, teacher_classes):
        # Check if the class code exists in the teacher's classes
        if class_code in teacher_classes:
            # Add the student to the class
            if class_code not in self.classes:
                self.classes[class_code] = []
            self.classes[class_code].append(self.username)
            return True
        else:
            return False

    def get_student_classes(self):
        return list(self.classes.keys())
