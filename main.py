def main():
    initialize.initialize_session_state()
    
    st.sidebar.title("Navigation")
    pages = ["Login", "Register"]
    if st.session_state.get("logged_in", False):
        if st.session_state.user_type == "teacher":
            pages.append("Teacher Homepage")
            teacher_instance = Teacher.get_teacher()
            for class_name in teacher_instance.get_teacher_classes():
                pages.append(class_name)
        elif st.session_state.user_type == "student":
            pages.append("Student Homepage")
            # Fetch the classes joined by the student
            student_instance = Student.get_student()
            for class_name in student_instance.get_student_classes():
                pages.append(class_name)

        if "selected_class" in st.session_state:
            pages.append("Class Page")

    page = st.sidebar.radio("Go to", pages)

    if page == "Login":
        login_page()
    elif page == "Register":
        register_page()
    elif page in ["Teacher Homepage", "Student Homepage"]:
        homepage(st.session_state.username, st.session_state.user_type)
    elif page == "Class Page":
        class_page(st.session_state.username, st.session_state.selected_class)
    else:
        if page in teacher_instance.get_teacher_classes():
            class_page(st.session_state.username, page)

if __name__ == "__main__":
    main()
