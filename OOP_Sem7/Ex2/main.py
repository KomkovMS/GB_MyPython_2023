class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

my_dog.make_sound() # Woof!
my_cat.make_sound() # Meow!
