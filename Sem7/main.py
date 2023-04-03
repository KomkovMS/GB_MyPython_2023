# class Car:
#     pass

# obj = Car()
# print(obj)      # Создание объекта <__main__.Car object at 0x000002EE4C3C06D0>
# print(type(obj))    # <class '__main__.Car'>
#
# obj_2 = Car()
# print(obj_2)      # Создание объекта <__main__.Car object at 0x00000263378D04D0>
# print(type(obj_2))    # <class '__main__.Car'>
#
# print(obj == obj_2) # False
# print(Car() == Car()) # False

# #################################################################

# class Car:
#     rule = 1
#     wheels = 4
#
#     # перегрузка метода инит
#     def __init__(self, color, engine):  # self - ссылка на объект
#         self.color = color
#         self.engine = engine
#
#
# obj = Car('red', 'gas')
# print(obj.rule, obj.wheels)  # Посмотреть атрибут:   # 1 4
#
# # поменять значения на уровне объекта
# obj.rule = 2
# obj.wheels = 6
# print(obj.rule, obj.wheels)  # Посмотреть атрибут:   # 2 6
# print(Car.rule, Car.wheels)  # 1 4 - на уровне класса не поменялось!!!
#
# print(obj.color, obj.engine, obj.wheels)  # red gas 6
#
# # атрибуты класса хранятся в словаре
# print(obj.__dict__) # {'color': 'red', 'engine': 'gas', 'rule': 2, 'wheels': 6}

# ########################################################################

class Car:
    # с начала атрибуты потом методы
    rule = 1
    wheels = 4

    # перегрузка метода инит
    # __подчеркивание справа и слева__ - это втсроенный метод, он не запускается
    # в ручную, он запускается при создании объекта
    def __init__(self, color, engine):  # self - ссылка на объект
        self.color = color
        self.engine = engine

    #
    def method(self, doors):
        self.doors = doors

# init возникает при создании объекта, если я эту строку запускаю происходи
# создание init
obj = Car('red', 'gas')

# атрибуты класса хранятся в словаре
print(obj.__dict__) # {'color': 'red', 'engine': 'gas'}

# атрибуты rule, wheels хранятся в классе
print(Car.__dict__) # {'__module__': '__main__', 'rule': 1, 'wheels': 4,
# '__init__': <function Car.__init__ at 0x000001C777939940>, '__dict__':
# <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute
# '__weakref__' of 'Car' objects>, '__doc__': None}

obj.method(4)
# теперь стало не 2 а 3 атрибута
print(obj.__dict__) # {'color': 'red', 'engine': 'gas', 'doors': 4}

# как вывести руль?
print(obj.rule)  # 1 - указано на уровне класса

