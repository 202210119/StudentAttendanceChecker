import streamlit as st
from authentication import logout
from teacher import Teacher
import pandas as pd
import datetime

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")

    # Display clock
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    st.header("Current Time:")
    st.write(current_time)

    # Display class selection
    selected_class = st.sidebar.selectbox("Select Class", ["Create New Class"] + Teacher.get_teacher_classes(username))

    if selected_class == "Create New Class":
        create_new_class(username)
    elif selected_class:
        display_class_schedule(selected_class)

def create_new_class(username):
    st.header("Create a New Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        teacher = Teacher(username)
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

def display_class_schedule(class_name):
    st.header(f"Class Schedule - {class_name}")
    schedule_df = pd.DataFrame(columns=["Time", "Event"], index=range(11))
    if st.checkbox("Edit Schedule"):
        schedule_df = st.dataframe(schedule_df, editable=True)
    else:
        st.dataframe(schedule_df)
