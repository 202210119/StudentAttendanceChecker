# teacher.py

import streamlit as st

class Teacher:
    @staticmethod
    def get_teacher():
        if "teacher" not in st.session_state:
            st.session_state.teacher = Teacher()
        return st.session_state.teacher

    def __init__(self):
        if "classes" not in st.session_state:
            st.session_state.classes = {}

    def create_class(self, class_name):
        if class_name == "":
            return False
        if class_name not in st.session_state.classes:
            st.session_state.classes[class_name] = {}
            return True
        else:
            return False

    def delete_class(self, class_name):
        if class_name in st.session_state.classes:
            del st.session_state.classes[class_name]
            return True
        else:
            return False

    def get_teacher_classes(self):
        return list(st.session_state.classes.keys())

    def get_class_schedule(self, class_name):
        return st.session_state.classes.get(class_name, {})

    def add_event_to_schedule(self, class_name, event_time, event_description):
        if class_name in st.session_state.classes:
            if event_time != "" and event_description != "":
                st.session_state.classes[class_name][event_time] = event_description
                return True
        return False
