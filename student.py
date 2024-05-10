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

    def get_student_classes(self):
        if st.session_state.classes:
            return [class_name for class_name, students in st.session_state.classes.items() if st.session_state.username in students]
        else:
            return []

def join_class(username):
    st.header("Join a Class")
    st.info("Select a class to join:")
    student = Student.get_student()  # Get the student instance
    existing_classes = student.get_student_classes()  # Use the Student class to get existing classes
    if existing_classes:
        selected_class = st.selectbox("Select Class", [""] + existing_classes)
        if selected_class:
            if st.button("Join Class"):
                if student.join_class(selected_class):
                    st.success(f"You have joined the class '{selected_class}'.")
                    st.session_state.selected_class = selected_class
                else:
                    st.error(f"Failed to join the class '{selected_class}'.")

    else:
        st.info("No classes available to join.")

    if st.button("Logout"):
        logout()
        st.experimental_rerun()
