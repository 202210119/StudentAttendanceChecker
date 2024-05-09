import streamlit as st

teacher_users = {}
student_users = {}

def register_teacher(username, password):
    if username in teacher_users:
        st.warning("Teacher account already exists! Please choose a different username.")
    else:
        teacher_users[username] = password
        st.success("Teacher account registration successful! You can now login.")

def register_student(username, password):
    if username in student_users:
        st.warning("Student account already exists! Please choose a different username.")
    else:
        student_users[username] = password
        st.success("Student account registration successful! You can now login.")

def login_teacher(username, password):
    if username in teacher_users and teacher_users[username] == password:
        st.success(f"Welcome back, Teacher {username}!")
        teacher_homepage(username)
    else:
        st.error("Invalid username or password for Teacher account. Please try again.")

def login_student(username, password):
    if username in student_users and student_users[username] == password:
        st.success(f"Welcome back, Student {username}!")
        student_homepage(username)
    else:
        st.error("Invalid username or password for Student account. Please try again.")

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")
    st.write("This is the Teacher homepage.")

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")
    st.write("This is the Student homepage.")

def main():
    st.title("Simple Login and Register App")

    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        account_type = st.radio("Account Type", ["Teacher", "Student"])
        if st.button("Login"):
            if account_type == "Teacher":
                login_teacher(username, password)
            elif account_type == "Student":
                login_student(username, password)

    elif choice == "Register":
        st.header("Register")
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

if __name__ == "__main__":
    main()
