# student.py

class Student:
    @staticmethod
    def get_student(username):
        if "student" not in st.session_state:
            st.session_state.student = Student()
        return st.session_state.student

    def __init__(self):
        if "classes" not in st.session_state:
            st.session_state.classes = {}

        self.classes = st.session_state.classes

    def join_class(self, class_name, teacher_classes):
        if class_name in teacher_classes:
            self.classes[class_name] = class_name
            return True 
        else:
            return False 

    def get_student_classes(self):
        return list(self.classes.keys())
