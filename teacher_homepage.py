import streamlit as st
from authentication import logout

def teacher_homepage():
    st.title(f"Welcome, Teacher {st.session_state.username}!")
    st.write("This is the Teacher homepage.")
