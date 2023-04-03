class User:
    def __init__(self, name):
        self.name = name

    def func(self):
        pass


class Teacher(User):
    def __init__(self, name, subject):
        super().__init__(name)

        self.subject = subject

    def func(self):
        pass


obj = Teacher('имя', 'math')
print(obj.func())
