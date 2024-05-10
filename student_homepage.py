import streamlit as st
from authentication import logout
import datetime
import time

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    current_time_placeholder = st.empty()

    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        st.success(f"You have joined the class with code '{class_code}'.")

    while True:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        current_time_placeholder.write(f"# Current Time:")
        current_time_placeholder.write(f"## {current_time}")
        time.sleep(1)
