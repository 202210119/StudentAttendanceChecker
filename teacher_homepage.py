# teacher_homepage.py
import streamlit as st
from authentication import logout
from teacher import Teacher

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")

    # Display option to create a new class
    st.header("Create a New Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        teacher = Teacher(username)
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

    # Display existing classes
    st.header("Your Classes")
    teacher = Teacher(username)
    existing_classes = teacher.get_teacher_classes()
    if existing_classes:
        selected_class = st.radio("Select Class", existing_classes)
        if st.button("Go to Class"):
            # Save the selected class in the session state for navigation
            st.session_state.selected_class = selected_class
            st.experimental_rerun()  # Rerun the app to switch to the class page
    else:
        st.info("You haven't created any classes yet.")
