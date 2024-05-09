import streamlit as st
from authentication import login

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.empty()
            st.success(f"Welcome, {st.session_state.user_type.capitalize()} {username}!")
