# Задача 1. Координаты точки
# В одной из практик предыдущего модуля была задача на реализацию класса «Точка». Модернизируйте класс
# по следующему условию: объект «Точка» на плоскости имеет координаты x и y; при создании новой точки могут
# передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
#
# 1. Предоставление информации о точке (используйте магический метод str).
# 2. Геттер и сеттер для x.
# 3. Геттер и сеттер для y.
#
# Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.


class Point:

    def __init__(self, x=0, y=0):
        self.__coord_x = x
        self.__coord_y = y

    def set_x(self, x):
        if not isinstance(x, int):
            raise Exception("Введенное значение не число")
        else:
            self.__coord_x = x

    def get_x(self):
        return self.__coord_x

    def set_y(self, y):
        if not isinstance(y, int):
            raise Exception("Введенное значение не число")
        else:
            self.__coord_y = y

    def get_y(self):
        return self.__coord_y

    def __str__(self):
        return f"Координаты точки Х: {self.__coord_x}\n" \
               f"Координаты точки Y: {self.__coord_y}"


point = Point()
print(point)

point.set_x(5)
print(point)
point.set_y(6)
print(point.get_y())
