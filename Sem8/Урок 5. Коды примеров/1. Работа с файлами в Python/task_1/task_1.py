"""Чтение данных из файла"""

# Метод read(). Позволяет прочитать файл целиком.
my_f = open("mtsuri.txt", "r", encoding='utf-8')
content = my_f.read()
print(content)
my_f.close()

print()

# Метод readline(). Позволяет извлечь очередную строку.
my_f = open("mtsuri.txt", "r", encoding='utf-8')
content = my_f.readline()
print(content)
my_f.close()

print()

# Метод readlines(). Позволяет извлечь и вывести полный список строк файла.
my_f = open("mtsuri.txt", "r", encoding='utf-8')
content = my_f.readlines()
print(content)
my_f.close()
