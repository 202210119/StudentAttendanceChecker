class Teacher:
    def __init__(self, username):
        self.username = username
        self.classes = {}

    def create_class(self, class_name):
        if class_name not in self.classes:
            self.classes[class_name] = {}
            return True
        else:
            return False

    def get_teacher_classes(self):
        return list(self.classes.keys())

    def get_class_schedule(self, class_name):
        return self.classes.get(class_name, {})
