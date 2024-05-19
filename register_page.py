import streamlit as st
from google_sheets import append_row

SHEET_NAME = "StudentAttendanceChecker"  # Your Google Sheets name
WORKSHEET_NAME = "Users"  # Your worksheet name

def register_page():
    st.title("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_type = st.selectbox("User Type", ["student", "teacher"])

    if st.button("Register"):
        new_user = [username, password, user_type]
        append_row(SHEET_NAME, WORKSHEET_NAME, new_user)
        st.success("Registration successful! Please log in.")

if __name__ == "__main__":
    register_page()
