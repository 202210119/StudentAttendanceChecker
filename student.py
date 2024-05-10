import streamlit as st

class Student:
    @staticmethod
    def get_student():
        if "student" not in st.session_state:
            st.session_state.student = Student()
        return st.session_state.student

    def __init__(self):
        if "classes" not in st.session_state:
            st.session_state.classes = {}  # Initialize classes if not already present

    def join_class(self, class_name):
        # Check if the class_name exists in the session state
        if class_name in st.session_state.classes:
            if st.session_state.username not in st.session_state.classes[class_name]:
                st.session_state.classes[class_name].append(st.session_state.username)  # Append username to the list
                return True  # Return True on successful join
            else:
                st.warning("You are already in this class.")
        else:
            st.warning("No classes available to join.")  # Warn if no classes are available to join
            return False  # Return False if no classes are available

        return False  # Return False if joining fails

    def get_student_classes(self):
        if st.session_state.classes:
            return list(st.session_state.classes.keys())  # Return all class names
        else:
            return []
