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
                # If the class exists and the student is not already in it, add the student
                if not isinstance(st.session_state.classes[class_name], list):
                    st.session_state.classes[class_name] = [st.session_state.classes[class_name]]  # Initialize as list
                st.session_state.classes[class_name].append(st.session_state.username)
                return True  # Return True on successful join
            else:
                st.warning("You are already in this class.")
        else:
            # If the class doesn't exist, create it and add the student
            st.session_state.classes[class_name] = [st.session_state.username]
            return True  # Return True on successful join

        return False  # Return False if joining fails

    def get_student_classes(self):
        return list(st.session_state.classes.keys())
