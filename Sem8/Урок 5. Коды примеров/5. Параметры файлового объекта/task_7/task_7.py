f_obj = open("new_f.txt", "w", encoding='utf-8')
print("Файл. Имя: ", f_obj.name)
print("Файл. Закрыт: ", f_obj.closed)
print("Файл. Режим: ", f_obj.mode)

"""
Файл. Имя:  new_f.txt
Файл. Закрыт:  False
Файл. Режим:  w
"""
