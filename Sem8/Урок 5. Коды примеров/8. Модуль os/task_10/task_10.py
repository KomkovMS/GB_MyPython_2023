# os.remove(). Отвечает за удаление указанного файла.
from os import remove, rename, listdir

remove("my_file.txt")

rename("test.txt", "pytest.txt")

content = listdir(path=".")
print(content)

content = listdir()
print(content)

content = listdir(path="..")
print(content)
