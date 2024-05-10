import streamlit as st
from authentication import logout
import pandas as pd

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    schedule_placeholder = st.empty()

    schedule_df = pd.DataFrame(columns=["Time", "Event"])

    st.header("Class Schedule")
    schedule_placeholder.table(schedule_df)
