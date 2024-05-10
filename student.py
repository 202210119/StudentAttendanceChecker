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
        # Check if the class_name exists in session state
        if class_name in st.session_state.classes:
            # Check if the student is already in the class
            if st.session_state.username not in st.session_state.classes[class_name]:
                # Add the student to the class
                st.session_state.classes[class_name].update(st.session_state.username)
                return True  # Return True on successful join
            else:
                st.warning("You are already in this class.")
        else:
            # If the class doesn't exist, create a new entry and add the student
            st.session_state.classes[class_name] = [st.session_state.username]
            return True  # Return True on successful join

        return False  # Return False if joining fails

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
