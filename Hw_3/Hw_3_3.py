"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.

Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456

"""


# def user_data(**kwargs):
#     return kwargs
#
#
# user = user_data(name='Иван', surname='Иванов', age=1846, residence='Москва',
#                  email='ackie@gmail.com', phone='01005321456')
# print(user)

def user_data(name, surname, age, residence, email, phone):
    print(
        f'{name} {surname} {age} года рождения, проживает в городе {residence},'
        f' email: {email}, телефон: {phone}')


user_data(name='Иван', surname='Иванов', age=1846, residence='Москва',
          email='ackie@gmail.com', phone='01005321456')
