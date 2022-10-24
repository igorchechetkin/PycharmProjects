# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.

from random import randint


class Toyota:

    car_color = "red"
    price = 1_000_000
    max_speed = 200
    fact_speed = 0


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()

car_1.fact_speed = randint(0, 200)
car_2.fact_speed = randint(0, 200)
car_3.fact_speed = randint(0, 200)

print(car_1.fact_speed, car_2.fact_speed, car_3.fact_speed)
print(Toyota.fact_speed)
