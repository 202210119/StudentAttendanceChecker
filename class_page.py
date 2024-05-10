# class_page.py
import streamlit as st
from authentication import logout
from teacher import Teacher
def class_page(username, class_name):
    st.title(f"Class: {class_name}")
    # Display option to create a new event
    st.header("Add Event to Schedule")
    event_time = st.text_input("Enter Event Time:")
    event_description = st.text_input("Enter Event Description:")
    if st.button("Add Event"):
        teacher = Teacher.get_teacher()
        if teacher.add_event_to_schedule(class_name, event_time, event_description):
            st.success("Event added successfully.")
    # Display class schedule
    st.header("Class Schedule")
    teacher = Teacher.get_teacher()
    class_schedule = teacher.get_class_schedule(class_name)
    st.write("Class Schedule data type:", type(class_schedule))  # Print data type
    if class_schedule:
        for event_time, event_description in class_schedule.items():
            st.write(f"- {event_time}: {event_description}")
    else:
        st.info("No events in the schedule yet.")
    # Option to delete the class
    if st.button("Delete Class"):
        teacher = Teacher.get_teacher()
        if teacher.delete_class(class_name):
            st.success(f"Class '{class_name}' deleted successfully.")
            st.experimental_rerun()  # Rerun the app to refresh the teacher homepage
        else:
            st.error(f"Failed to delete class '{class_name}'.")
