
f_obj = open("mtsuri.txt", "r", encoding='utf-8')
content = f_obj.read()
print(content)
content = f_obj.read()
print(f'Пустая строка - {content}')
f_obj.close()

print()

f_obj = open("mtsuri.txt", "r", encoding='utf-8')
f_obj.read(10)
print("Текущая позиция:", f_obj.tell())
f_obj.close()

print()

f_obj = open("mtsuri.txt", "r", encoding='utf-8')
print(f_obj.read(3))
print("Мы находимся на позиции: ", f_obj.tell())
# Перемещаемся в начало
f_obj.seek(0)
print(f_obj.read(10))
f_obj.close()
