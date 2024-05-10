# student.py
import streamlit as st

class Student:
    @staticmethod
    def get_student():
        if "student" not in st.session_state:
            st.session_state.student = Student()
        return st.session_state.student

    def __init__(self):
        if "joined_classes" not in st.session_state:
            st.session_state.joined_classes = {}

    def join_class(self, class_name, class_code, teacher_classes):
        if class_name in teacher_classes:
            teacher_classes[class_name].append(self.username)
            return True
        else:
            return False

    def get_student_classes(self):
        return list(st.session_state.joined_classes.keys())

    def get_class_schedule(self, class_name):
        return st.session_state.joined_classes.get(class_name, {})

    def add_event_to_schedule(self, class_name, event_time, event_description):
        if class_name in st.session_state.joined_classes:
            if event_time != "" and event_description != "":
                st.session_state.joined_classes[class_name][event_time] = event_description
                return True
        return False
