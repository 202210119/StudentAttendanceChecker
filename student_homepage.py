import streamlit as st
from authentication import logout

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")
    
    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        st.success(f"You have joined the class with code '{class_code}'.")
