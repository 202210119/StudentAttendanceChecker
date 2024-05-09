import streamlit as st
from authentication import logout

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")
    st.write("This is the Student homepage.")
    if st.button("Logout"):
        logout()
        st.success("You have been logged out.")