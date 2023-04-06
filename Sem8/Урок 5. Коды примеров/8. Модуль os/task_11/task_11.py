"""os.path"""
from os.path import basename, dirname, exists, isdir, isfile, join, split

# os.path.basename(). Возвращает название файла пути
print(basename(r"C:\Users\Администратор\settings.py"))  # -> settings.py

# os.path.dirname(). Возвращает часть каталога пути
print(dirname(r"C:\Users\Администратор\settings.py"))  # -> C:\Users\Администратор

# os.path.exists(). Проверяет, существует ли указанный файл
print(exists(r"C:\Users\Администратор\settings.py"))  # -> False

# os.path.isdir(), os.path.isfile(). Проверяет, является ли объект папкой или файлом
print(isdir(r"C:\Users\Администратор\settings.py"))  # -> False
print(isfile(r"C:\Users\Администратор\settings.py"))  # -> False

# os.path.join(). Позволяет объединить несколько путей
print(join(r"C:\Users\Администратор", "settings.py"))  # -> C:\Users\Администратор\settings.py

# os.path.split(). Разделяет путь на кортеж, содержащий и путь до каталога, и имя файла
print(split(r"C:\Users\Администратор\settings.py"))  # -> ('C:\\Users\\Администратор', 'settings.py')
