import streamlit as st

def initialize_session_state():
    if "teacher_users" not in st.session_state:
        st.session_state.teacher_users = {}
    if "student_users" not in st.session_state:
        st.session_state.student_users = {}

def register_teacher(username, password):
    if username in st.session_state.teacher_users:
        st.warning("Teacher account already exists! Please choose a different username.")
    else:
        st.session_state.teacher_users[username] = password
        st.success("Teacher account registration successful! You can now login.")

def register_student(username, password):
    if username in st.session_state.student_users:
        st.warning("Student account already exists! Please choose a different username.")
    else:
        st.session_state.student_users[username] = password
        st.success("Student account registration successful! You can now login.")

def login(username, password):
    if username in st.session_state.teacher_users and st.session_state.teacher_users[username] == password:
        st.session_state.page = "teacher_homepage"
        st.success(f"Welcome back, Teacher {username}!")
    elif username in st.session_state.student_users and st.session_state.student_users[username] == password:
        st.session_state.page = "student_homepage"
        st.success(f"Welcome back, Student {username}!")
    else:
        st.error("Invalid username or password. Please try again.")

def teacher_homepage(username):
    st.title(f"Welcome, Teacher {username}!")
    st.write("This is the Teacher homepage.")
    if st.button("Logout"):
        st.session_state.pop("page")
        st.experimental_rerun()

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")
    st.write("This is the Student homepage.")
    if st.button("Logout"):
        st.session_state.pop("page")
        st.experimental_rerun()

def main():
    initialize_session_state()
    
    st.title("Simple Login and Register App")

    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            login(username, password)
            if "page" in st.session_state:
                if st.session_state.page == "teacher_homepage":
                    teacher_homepage(username)
                elif st.session_state.page == "student_homepage":
                    student_homepage(username)

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
