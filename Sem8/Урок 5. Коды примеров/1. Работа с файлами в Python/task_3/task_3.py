"""Запись данных в файл"""

# write
out_f = open("out_file.txt", "w", encoding='utf-8')
out_f.write("String string string")
out_f.close()

# writelines
out_f = open("out_file.txt", "w", encoding='utf-8')
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
out_f.writelines(str_list)
out_f.close()
