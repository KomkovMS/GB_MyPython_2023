
numb_1 = float(input("Введите первое вещественное число: "))
numb_2 = float(input("Введите второе вещественное число: "))

if numb_1 >= numb_2:
    print("Первая ветвь")
    if numb_1 > numb_2:
        print("Первое число больше второго")
    else:
        print("Числа равны")
elif numb_1 <= numb_2:
    print("Вторая ветвь")
    if numb_1 < numb_2:
        print("Первое число меньше второго")
    else:
        print("Числа равны")
