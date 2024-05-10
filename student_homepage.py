import streamlit as st
from authentication import logout
import pandas as pd
import requests

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    schedule_placeholder = st.empty()
    current_time_placeholder = st.empty()

    schedule_df = pd.DataFrame(columns=["Time", "Event"], index=range(11))

    st.header("Class Schedule")
    schedule_placeholder.table(schedule_df)

    while True:
        current_time = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC").json()["datetime"]
        current_time = pd.to_datetime(current_time)
        current_time = current_time.strftime("%I:%M:%S %p")
        current_time_placeholder.write(f"## Current Time: {current_time}")

