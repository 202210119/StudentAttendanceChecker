import streamlit as st
from authentication import login, logout

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.session_state.get("logged_in", False):
        if st.button("Logout"):
            logout()
            st.ererun()
    else:
        if st.button("Login"):
            if login(username, password):
                st.rerun()
