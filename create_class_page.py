import streamlit as st
from teacher import Teacher

def create_class_page():
    st.title("Create Class")

    teacher = Teacher.get_teacher()

    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")
