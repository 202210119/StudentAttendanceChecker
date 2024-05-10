import streamlit as st
from authentication import logout
from teacher import Teacher
import datetime

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")

    st.write("# Current Time:")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    st.write(f"## {current_time}")

    st.header("Create a Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        teacher = Teacher(username)
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")
