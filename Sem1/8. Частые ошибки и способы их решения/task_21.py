# Проблема 1. TypeError: Can't convert 'int' object to str implicitly

my_var = input("Введите число: ") + 5
print(my_var)
# Ошибка:
# TypeError: can only concatenate str (not "int") to str

my_var = int(input("Введите число: ")) + 5
print(my_var)
