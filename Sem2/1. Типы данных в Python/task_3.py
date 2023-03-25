"""Механизмы реверса строк"""

# 1)Срез

string = "abrakadbra"
str_reverse = string[::-1]
print(str_reverse)  # -> arbdakarba

# 2)Обратная итерация

for el in reversed("abrakadbra"):
    print(el)

# 3)Реверс на месте

string = "abrakadabra"
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(string) - el - 1]
    symbols[len(string) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse)
