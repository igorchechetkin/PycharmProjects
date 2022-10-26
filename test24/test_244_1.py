# Задача 1. Машина 3
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
#
# Четыре атрибута:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса
# (то есть передаваться в init). Реализуйте такое изменение класса.

class Toyota:

    def __init__(self, color, price, max_speed, speed):
        self.car_color = color
        self.price = price
        self.max_speed = max_speed
        self.fact_speed = speed

    def print_info(self):
        print(f"Color: {self.car_color}\nPrice: {self.price}\nMax speed: {self.max_speed}\n"
              f"Actual speed: {self.fact_speed}")

    def change_speed(self, speed):
        self.fact_speed = speed


car_1 = Toyota('red', 1_000_000, 200, 137)
car_1.print_info()
