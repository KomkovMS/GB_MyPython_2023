"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
за проезд и получали билет с номером. Счастливым билетом называют такой билет
с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no

"""

ticket_number = input('Введите шестизначный номер билета: ')

left_ticket_number = ticket_number[:3]
right_ticket_number = ticket_number[3:]

sum_left = 0
sum_right = 0

for num in left_ticket_number:
    sum_left += int(num)

for num in right_ticket_number:
    sum_right += int(num)

if sum_left == sum_right:
    print(f'{ticket_number} -> yes')
else:
    print(f'{ticket_number} -> no')


# другое решение:
def find_sum(num):
    sum_ = 0
    while num > 0:
        last_digit = num % 10  # получаем последнюю цифру
        sum_ += last_digit
        num = num // 10  # отсекает последнюю цифру
    return sum_


ticket = input('Введите номер билета: ')

if find_sum(int(ticket[:3])) == find_sum(int(ticket[-3:])):
    print("yes")
else:
    print("no")
