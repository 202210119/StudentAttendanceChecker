import streamlit as st
from google_sheets import get_all_records, append_row
from authentication import login, logout

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.session_state.get("logged_in", False):
        st.info(f"You are logged in as {st.session_state.user_type.capitalize()}")
        if st.button("Logout"):
            logout()
            st.rerun()
    else:
        if st.button("Login"):
            if login(username, password):
                st.rerun()
