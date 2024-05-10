class Student:
    @staticmethod
    def get_student():
        if "student" not in st.session_state:
            st.session_state.student = Student()
        return st.session_state.student

    def __init__(self):
        if "classes" not in st.session_state:
            st.session_state.classes = {}  # Dictionary to store class information

    def join_class(self, class_name):
        # Check if the class_name exists
        if class_name in st.session_state.classes:
            if st.session_state.username not in st.session_state.classes[class_name]:
                st.session_state.classes[class_name].append(st.session_state.username)
                return True  # Return True on successful join
            else:
                st.warning("You are already in this class.")
        else:
            st.session_state.classes[class_name] = [st.session_state.username]
            return True  # Return True on successful join

        return False  # Return False if joining fails

    def get_student_classes(self):
        return list(st.session_state.classes.keys())  # Return list of class names

    def get_all_enrolled_students(self):
        all_students = []
        for class_name, enrolled_users in st.session_state.classes.items():
            all_students.extend(enrolled_users)  # Extend the list with all usernames
        return all_students
