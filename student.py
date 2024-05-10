import streamlit as st
from teacher import Teacher

class Student:
    @staticmethod
    def get_student(username):
        if "students" not in st.session_state:
            st.session_state.students = {}
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
                self._update_student_classes(class_code)
                return True
        return False

    def _update_student_classes(self, class_code):
        if "students" not in st.session_state:
            st.session_state.students = {}
        students = st.session_state.students
        if self.username not in students:
            students[self.username] = {"classes": {}}
        student_data = students[self.username]
        student_data["classes"][class_code] = True

    def get_student_classes(self):
        student_data = self.get_student(self.username)
        if student_data is None:
            return []
        return list(student_data.get("classes", {}).keys())
