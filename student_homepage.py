import streamlit as st
from authentication import logout
import pandas as pd
import datetime
import time

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    schedule_placeholder = st.empty()
    current_time_placeholder = st.empty()

    schedule_df = pd.DataFrame(columns=["Time", "Event"])

    st.header("Class Schedule")
    schedule_placeholder.table(schedule_df)

    while True:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        current_time_placeholder.write(f"# Current Time:")
        current_time_placeholder.write(f"## {current_time}")
        time.sleep(1)
