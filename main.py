import streamlit as st
import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                account_type TEXT
                )""")
    conn.commit()
    conn.close()

# Function to register new users
def register(username, password, account_type):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, account_type) VALUES (?, ?, ?)",
                  (username, password, account_type))
        conn.commit()
        st.success("Registration successful! You can now login.")
    except sqlite3.IntegrityError:
        st.warning("Username already exists! Please choose a different username.")
    conn.close()

# Function to authenticate users
def login(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        st.success(f"Welcome back, {user[3]} {user[1]}!")
        if user[3] == "Teacher":
            teacher_homepage(user[1])
        elif user[3] == "Student":
            student_homepage(user[1])
    else:
        st.error("Invalid username or password. Please try again.")

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")
    st.write("This is the Teacher homepage.")

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")
    st.write("This is the Student homepage.")

def main():
    create_table()
    
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
        account_type = st.radio("Account Type", ["Teacher", "Student"])
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if new_password == confirm_password:
            if st.button("Register"):
                register(new_username, new_password, account_type)
        else:
            st.warning("Passwords do not match.")

if __name__ == "__main__":
    main()
