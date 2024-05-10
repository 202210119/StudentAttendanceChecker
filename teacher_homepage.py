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
        teacher = Teacher.get_teacher()
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

    # Display existing classes and option to delete
    st.header("Your Classes")
    teacher = Teacher.get_teacher()
    existing_classes = teacher.get_teacher_classes()
    if existing_classes:
        selected_class = st.selectbox("Select Class to Manage", [""] + existing_classes)
        if selected_class:
            if st.button("Go to Class"):
                st.session_state.selected_class = selected_class
                st.experimental_rerun()
        
        # Option to delete class
        class_to_delete = st.selectbox("Select Class to Delete", [""] + existing_classes)
        if class_to_delete:
            if st.button("Delete Class"):
                if teacher.delete_class(class_to_delete):
                    st.success(f"Class '{class_to_delete}' deleted successfully.")
                    st.experimental_rerun()  # Rerun the app to refresh the teacher homepage
                else:
                    st.error(f"Failed to delete class '{class_to_delete}'.")
    else:
        st.info("You haven't created any classes yet.")
