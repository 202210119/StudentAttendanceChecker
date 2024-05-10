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
        if st.session_state.username not in st.session_state.classes[class_name]:
            st.session_state.classes[class_name] += [st.session_state.username]
            return True
        else:
            st.warning("You are already in this class.")
    else:
        st.session_state.classes[class_name] = [st.session_state.username]
        return True

    return False

def get_available_classes(self):
    all_classes = st.session_state.classes.keys()
    joined_classes = self.get_student_classes()
    return [class_name for class_name in all_classes if class_name not in joined_classes]
