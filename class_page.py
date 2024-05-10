# class_page.py
import streamlit as st
import pandas as pd
import datetime

def class_page(class_name):
    st.title(f"Class: {class_name}")

    # Display clock
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    st.header("Current Time:")
    st.write(current_time)

    # Display class schedule
    st.header("Class Schedule")
    schedule_df = pd.DataFrame(columns=["Time", "Event"], index=range(11))
    if st.checkbox("Edit Schedule"):
        schedule_df = st.dataframe(schedule_df, editable=True)
    else:
        st.dataframe(schedule_df)
