import streamlit as st
from authentication import logout
import datetime

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    st.write("# Current Time:")
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    st.write(f"## {current_time}")

    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        st.success(f"You have joined the class with code '{class_code}'.")
