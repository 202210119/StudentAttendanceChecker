import streamlit as st
from authentication import logout
from teacher import Teacher
import pandas as pd
import requests

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")

    schedule_placeholder = st.empty()
    current_time_placeholder = st.empty()

    schedule_df = pd.DataFrame(columns=["Time", "Event"], index=range(11))

    st.header("Create a Class")
    class_name = st.text_input("Enter Class Name:")
    if st.button("Create"):
        teacher = Teacher(username)
        if teacher.create_class(class_name):
            st.success(f"Class '{class_name}' created successfully.")

    st.header("Schedule")
    if st.session_state.page == "Teacher Homepage":
        if st.checkbox("Edit Schedule"):
            schedule_df = st.dataframe(schedule_df, editable=True)
        else:
            st.dataframe(schedule_df)
    else:
        st.dataframe(schedule_df)

    while True:
        current_time = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC").json()["datetime"]
        current_time = pd.to_datetime(current_time)
        current_time = current_time.strftime("%I:%M:%S %p")
        current_time_placeholder.write(f"## Current Time: {current_time}")
