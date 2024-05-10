class Teacher:
    def __init__(self, username):
        self.username = username
        self.classes = {}

    def create_class(self, class_name):
        if class_name in self.classes:
            return False
        else:
            self.classes[class_name] = []
            return True

    def get_classes(self):
        return list(self.classes.keys())
