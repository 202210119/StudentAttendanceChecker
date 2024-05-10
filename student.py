class Student:
    def __init__(self, username):
        self.username = username

    def join_class(self, class_name, class_code, teacher_classes):
        if class_name in teacher_classes:
            teacher_classes[class_name].append(self.username) 
            return True 
        else:
            return False 
