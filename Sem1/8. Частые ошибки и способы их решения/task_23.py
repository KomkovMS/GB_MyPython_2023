# Проблема 3. SyntaxError: invalid syntax
msg = True
if msg = True:
    print("Приветственное сообщение")
# Ошибка:
# SyntaxError: invalid syntax

msg = True
if msg == True:
    print("Приветственное сообщение")
