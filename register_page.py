# register_page.py

import streamlit as st
from authentication import register_teacher, register_student

def register_page():
    st.title("Register")
    account_type = st.radio("Account Type", ["Teacher", "Student"])
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if new_password == confirm_password:
        if st.button("Register"):
            if account_type == "Teacher":
                register_teacher(new_username, new_password)
            elif account_type == "Student":
                register_student(new_username, new_password)
    else:
        st.warning("Passwords do not match.")
