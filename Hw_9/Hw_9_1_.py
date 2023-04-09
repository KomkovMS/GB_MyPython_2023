"""
Реализовать дескрипторы для любых двух классов
"""


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        instance._name = value


class SurnameDescriptor:
    def __get__(self, instance, owner):
        return instance._surname

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Фамилия должна быть строкой")
        instance._surname = value


class PositionDescriptor:
    def __get__(self, instance, owner):
        return instance._position

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Позиция должна быть строкой")
        instance._position = value


class IncomeDescriptor:
    def __get__(self, instance, owner):
        return instance._income

    def __set__(self, instance, value):
        if not isinstance(value, dict):
            raise TypeError("Доход должен быть словарем")
        if "wage" not in value or "bonus" not in value:
            raise ValueError("Доход должен содержать «зарплату» и «премию")
        instance._income = value


class Worker:
    name = NameDescriptor()
    surname = SurnameDescriptor()
    position = PositionDescriptor()
    income = IncomeDescriptor()

    def __init__(self, name, surname, position, income):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __str__(self):
        return f'{self.get_full_name()}, {self.position}, ' \
               f'{self.get_total_income()}'


my_obj = Position('Maksim', 'Komkov', 'engineer',
                  {"wage": 20000, "bonus": 10000})

print(my_obj.name)
my_obj.name = "Alex"
print(my_obj.name)

print(my_obj.surname)
my_obj.surname = 123
print(my_obj.surname)

print(my_obj.position)
my_obj.position = 123
print(my_obj.position)

print(my_obj.income)
my_obj.income = "not a dict"
print(my_obj.income)

my_obj.income = {"wage": 30000}
print(my_obj.income)

print(my_obj.get_full_name())
print(my_obj.get_total_income())
print(my_obj)
