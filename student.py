import streamlit as st
from teacher import Teacher

class Student:
    @staticmethod
    def get_student(username):
        if "students" not in st.session_state:
            return None
        students = st.session_state.students
        return students.get(username)

    def __init__(self, username):
        self.username = username

    def join_class(self, class_code):
        teacher = Teacher.get_teacher()
        teacher_classes = teacher.get_teacher_classes()
        if class_code in teacher_classes:
            if self.username not in teacher_classes[class_code]:
                teacher_classes[class_code].append(self.username)
                return True
        return False

    def get_student_classes(self):
        if "students" not in st.session_state:
            return []
        students = st.session_state.students
        student_data = students.get(self.username, {})
        return list(student_data.get("classes", {}).keys())
