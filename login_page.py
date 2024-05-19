import streamlit as st
from google_sheets import get_all_records, append_row

SHEET_NAME = "StudentAttendanceChecker"  # Your Google Sheets name
WORKSHEET_NAME = "Users" 

def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.session_state.get("logged_in", False):
        st.info(f"You are logged in as {st.session_state.user_type.capitalize()}")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()
    else:
        if st.button("Login"):
            users = get_all_records(SHEET_NAME, WORKSHEET_NAME)
            for user in users:
                if user["username"] == username and user["password"] == password:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.session_state["user_type"] = user["user_type"]
                    st.experimental_rerun()
            st.error("Invalid username or password")

    if st.button("Register"):
        st.write("Please use the registration page to sign up.")

if __name__ == "__main__":
    login_page()
