import streamlit as st
from authentication import logout
from teacher import Teacher
import pandas as pd
import requests
import datetime

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")

    schedule_placeholder = st.empty()
    current_time_placeholder = st.empty()

    schedule_df = pd.DataFrame(columns=["Time", "Event"])

    st.header("Create a Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        teacher = Teacher(username)
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

    st.header("Schedule")
    time = st.text_input("Enter Time:")
    event = st.text_input("Enter Event:")
    if st.button("Add Event"):
        schedule_df = schedule_df.append({"Time": time, "Event": event}, ignore_index=True)

    schedule_placeholder.table(schedule_df)

    while True:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        current_time_placeholder.write(f"## Current Time: {current_time}")
