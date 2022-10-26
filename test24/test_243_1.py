# Задача 1. Машина 2
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
# Добавьте два метода класса:
#
# 1. Отображение информации об объекте класса.
# 2. Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

class Toyota:

    car_color = "red"
    price = 1_000_000
    max_speed = 200
    fact_speed = 0

    def print_info(self):
        print(f"Color: {self.car_color}\nPrice: {self.price}\nMax speed: {self.max_speed}\n"
              f"Actual speed: {self.fact_speed}")

    def change_speed(self, speed):
        self.fact_speed = speed


car_1 = Toyota()
car_1.print_info()
car_1.change_speed(100)
print(f"\nActual speed were changer to {car_1.fact_speed}km/h")
