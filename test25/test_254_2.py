# Задача 2. Полёт
# Иногда для реализации дочерних классов используется так называемый класс-роль, где также описываются общие
# атрибуты и методы, но в программе инициализируются объекты только дочерних классов, а базовый класс-роль
# не трогается. К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться.
#
# Реализуйте класс «Может летать».
#
# Атрибуты:
#
# Высота = 0.
# Скорость = 0.
# Методы:
#
# Взлететь (в теле прописать pass).
# Лететь (в теле прописать pass).
# Приземлиться (установить высоту и скорость в значение 0).
# Вывести высоту и скорость на экран.
#
# Затем реализуйте два дочерних класса:
#
# «Бабочка», который может:
#
# Взлететь (высота = 1).
# Лететь (скорость = 0.5).
# «Ракета», которая может:
#
# Взлететь (высота = 500, скорость = 1000).
# Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).

class CanFly:

    def __init__(self):
        self.altitude = 0
        self.velocity = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def landing(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return f"Высота: {self.altitude}\nСкорость: {self.velocity}"


class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.5


class Missile(CanFly):

    def take_off(self):
        self.altitude = 500
        self.velocity = 1000

    def landing(self):
        self.altitude = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print("Ракета показала себя великолепно. Только упала не на ту планету (C) Вернер фон Браун")


butterfly = Butterfly()
missile = Missile()

butterfly.take_off()
print(butterfly)
butterfly.fly()
print(butterfly)

missile.take_off()
print(missile)
missile.landing()
print(missile)
