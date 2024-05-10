import streamlit as st
from authentication import logout
from teacher import Teacher
import datetime
import time

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")

    current_time_placeholder = st.empty()

    st.header("Create a Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        teacher = Teacher(username)
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

    while True:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        current_time_placeholder.write(f"# Current Time:")
        current_time_placeholder.write(f"## {current_time}")
        time.sleep(1)
