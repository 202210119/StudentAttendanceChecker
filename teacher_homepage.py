import streamlit as st
from authentication import logout
from teacher import Teacher

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")

    st.header("Create a New Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        teacher = Teacher(username)
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

    # Display existing classes
    teacher = Teacher(username)
    existing_classes = teacher.get_teacher_classes()
    if existing_classes:
        st.header("Your Classes")
        selected_class = st.radio("Select Class", existing_classes)
        if st.button("Go to Class"):
            st.session_state.selected_class = selected_class
            st.experimental_rerun()
    else:
        st.info("You haven't created any classes yet.")
