import streamlit as st
from teacher import Teacher  # Assuming Teacher class is defined elsewhere

class Student:
  @staticmethod
  def get_student(username):
    if "student" not in st.session_state:
      st.session_state.student = Student()
    return st.session_state.student

  def __init__(self):
    if "classes" not in st.session_state:
      st.session_state.classes = {}  # Initialize as an empty dictionary

  def join_class(self, class_code, teacher_classes):
    if class_code in teacher_classes:
      if class_code not in st.session_state.classes:
        st.session_state.classes[class_code] = []  # Create an empty list for the new class code
      st.session_state.classes[class_code].append(st.session_state.username)  # Add username to the list
      return True
    else:
      return False

  def get_student_classes(self):
    return list(st.session_state.classes.keys())
