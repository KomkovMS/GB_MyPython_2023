"""Оператор is"""

a = [10, 20, 30, 40]
b = [10, 20, 30, 40]

if a is b:
    print("Переменные идентичны")
else:
    print("Переменные не идентичны")

'''Переменные идентичны'''


obj_1 = [10, 20, 30, 40]
obj_2 = obj_1
print(obj_1 == obj_2)  # -> True
print(obj_1 is obj_2)  # -> True

obj_2 = obj_1[:]  # переменная obj_2 ссылается на копию obj_1
print(obj_1 == obj_2)  # -> True
print(obj_1 is obj_2)  # -> False
print(obj_1 is not obj_2)  # -> True

obj_1 = None
print(obj_1 is None)  # -> True
