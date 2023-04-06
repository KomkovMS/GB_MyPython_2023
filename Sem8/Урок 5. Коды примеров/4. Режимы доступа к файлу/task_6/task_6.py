# Режим x
f_1 = open("my_file.txt", 'w', encoding='utf-8')
f_2 = open("my_file.txt", 'x', encoding='utf-8')  # -> FileExistsError: [Errno 17] File exists: 'my_file.txt'

# Режим a
f_obj = open("new_f.txt", 'a', encoding='utf-8')
f_obj.write("My string")
f_obj.close()

# Режим b
f_obj = open("data.bin", "wb", encoding='utf-8')
my_var = "if5s"
f_obj.write(my_var)
f_obj.close()

# Режим +
with open("file.dat", "r+", encoding='utf-8') as f_obj:
    f_obj.write("another string")
    content = f_obj.read()
    print(content)
