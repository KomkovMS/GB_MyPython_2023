class Car:
    def __init__(self, model, year):
        self.__make = 42
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine has started.")

    def getMake(self):
        return self.__make


my_car = Car("Camry", 2020)
print(my_car.getMake())  # 42
# my_car.__dict__['__make'] = 35
print(my_car.model)  # Camry
print(my_car.year)  # 2020
my_car.start_engine()  # The engine has started.
