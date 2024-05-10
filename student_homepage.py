import streamlit as st
from authentication import logout
from student import Student  # Import the Student class directly from Student.py

def student_homepage(username):
    st.title(f"Welcome, Student {username}!")

    st.header("Join a Class")
    class_code = st.text_input("Enter Class Code:")
    if st.button("Join"):
        student = Student(username)
        if student.join_class(class_code):
            st.success(f"You have joined the class with code '{class_code}'.")

    # Display the classes the student has joined
    student_instance = Student.get_student(username)
    student_classes = student_instance.get_student_classes()

    st.header("Your Classes")
    if student_classes:
        for class_name in student_classes:
            st.write(class_name)
    else:
        st.write("You haven't joined any classes yet.")

    if st.button("Logout"):
        logout()
        st.experimental_rerun()
