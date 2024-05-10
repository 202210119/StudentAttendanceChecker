import streamlit as st
from authentication import logout
from student import Student

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        student = Student.get_student(username)
        if student is not None:
            if student.join_class(class_code):
                st.success(f"You have joined the class with code '{class_code}'.")
            else:
                st.error("Invalid class code.")

    student = Student.get_student(username)
    if student is not None:
        student_classes = student.get_student_classes()
        st.header("Your Classes")
        if student_classes:
            for class_name in student_classes:
                st.write(class_name)
        else:
            st.write("You haven't joined any classes yet.")

    if st.button("Logout"):
        logout()
        st.experimental_rerun()
