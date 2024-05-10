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
        # Check if the class_name exists in the session state
        if class_name in st.session_state.classes:
            if st.session_state.username not in st.session_state.classes[class_name]:
                st.session_state.classes[class_name] = [st.session_state.username]  # Create a list with username
                return True  # Return True on successful join
            else:
                st.warning("You are already in this class.")
        else:
            st.session_state.classes[class_name] = [st.session_state.username]  # Create a new class entry with username list
            return True  # Return True on successful join

        return False  # Return False if joining fails

def get_student_classes(self):
    if "username" not in st.session_state:
        return []

    student_username = st.session_state.username
    return [class_name for class_name, students in st.session_state.classes.items() if student_username in students]
