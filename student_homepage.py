import streamlit as st
from authentication import logout

def student_homepage():
    st.title(f"Welcome, Student {st.session_state.username}!")
    st.write("This is the Student homepage.")
