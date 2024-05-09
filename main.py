import streamlit as st

users = {}

# Function to register new users
def register(username, password):
    if username in users:
        st.warning("User already exists! Please choose a different username.")
    else:
        users[username] = password
        st.success("Registration successful! You can now login.")

# Function to authenticate users
def login(username, password):
    if username in users and users[username] == password:
        st.success(f"Welcome back, {username}!")
    else:
        st.error("Invalid username or password. Please try again.")

def main():
    st.title("Simple Login and Register App")

    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            login(username, password)

    elif choice == "Register":
        st.header("Register")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if new_password == confirm_password:
            if st.button("Register"):
                register(new_username, new_password)
        else:
            st.warning("Passwords do not match.")

if __name__ == "__main__":
    main()
