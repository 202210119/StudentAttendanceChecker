import streamlit as st
from authentication import logout

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")
    st.write("This is the Teacher homepage.")
    if st.button("Logout"):
        logout()
        st.success("You have been logged out.")