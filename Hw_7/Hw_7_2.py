"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 0.05

    def mass_calculation(self):
        mass = self._length * self._width * self.weight * self.thickness
        return int(mass)


my_obj = Road(5000, 20)
mass_calc = my_obj.mass_calculation()
print(type(mass_calc))
print(
    f'Масса асфальта, необходимого для покрытия всего дорожного полотна: '
    f'{my_obj._length}м*{my_obj._width}м*{my_obj.weight}кг*'
    f'{my_obj.thickness}м = {my_obj.mass_calculation()} кг = '
    f'{int(my_obj.mass_calculation() / 1000)} тонн.')
