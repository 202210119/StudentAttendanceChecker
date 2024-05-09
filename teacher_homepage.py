import streamlit as st
from authentication import logout

def teacher_homepage():
    st.title(f"Welcome, Teacher {st.session_state.username}!")
    st.write("This is the Teacher homepage.")
    if st.button("Logout"):
        logout()
        st.experimental_rerun()  # Rerun the app to show the login page
