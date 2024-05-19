import streamlit as st
from google_sheets import get_all_records, append_row
from authentication import logout

SHEET_NAME = "StudentAttendanceChecker"
CLASSES_WORKSHEET = "Classes"

def homepage(username, user_type):
    st.title(f"Welcome, {user_type.capitalize()} {username}!")

    if user_type == "teacher":
        create_teacher_class(username)
    elif user_type == "student":
        join_class(username)

def create_teacher_class(username):
    st.header("Create a New Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create Class"):
        append_row(SHEET_NAME, CLASSES_WORKSHEET, [username, class_name])
        st.success(f"Class '{class_name}' created successfully.")

    st.header("Your Classes")
    classes = get_all_records(SHEET_NAME, CLASSES_WORKSHEET)
    teacher_classes = [cls["class_name"] for cls in classes if cls["teacher"] == username]

    if teacher_classes:
        selected_class = st.selectbox("Select Class", [""] + teacher_classes)
        if selected_class:
            if st.button("Go to Class"):
                st.session_state.selected_class = selected_class
                st.experimental_rerun()
    else:
        st.info("You haven't created any classes yet.")

def join_class(username):
    st.header("Join a Class")
    st.info("Select a class to join:")

    classes = get_all_records(SHEET_NAME, CLASSES_WORKSHEET)
    class_names = [cls["class_name"] for cls in classes]

    if class_names:
        selected_class = st.selectbox("Select Class", [""] + class_names)
        if selected_class:
            if st.button("Join Class"):
                # Here you could add the logic to associate the student with the class in your Google Sheet
                st.success(f"You have joined the class '{selected_class}'.")
                st.experimental_rerun()

    if st.button("Logout"):
        logout()
        st.experimental_rerun()

if __name__ == "__main__":
    homepage()
