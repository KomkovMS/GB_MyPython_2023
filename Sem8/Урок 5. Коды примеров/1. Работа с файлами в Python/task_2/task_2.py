"""Чтение данных из файла"""

my_f = open("mtsuri.txt", "r", encoding='utf-8')

for line in my_f:
    print(line)

my_f.close()

print()

my_f = open("mtsuri.txt", "r", encoding='utf-8')

while True:
    content = my_f.read(1024)
    print(content)

    if not content:
        break
