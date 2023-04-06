try:
    f_obj = open("mtsuri.txt", encoding='utf-8')
    for line in f_obj:
        print(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()


try:
    with open("mtsuri.txt", encoding='utf-8') as f_obj:
        for line in f_obj:
            print(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")
