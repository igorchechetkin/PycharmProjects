# Задача 1. Корабли
# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый может
# сделать два действия: сообщить свою модель и идти по воде.
#
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю. У него есть ещё
# два действия: погрузить и выгрузить груз с корабля.
#
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью. Также,
# вместо погрузки и выгрузки, у него есть другое действие — атаковать.
#
# Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный
# класс «Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.

class Ship:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Модель корабля: {self.model}"

    def sail(self):
        print("Корабль куда-то поплыл")


class WarShip(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print(f"\nКорабль атакует из орудия {self.gun}")


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print("\nЗагружаем корабль.")
        self.tonnage_load += 1
        print(f"Текущая загруженность корабля: {self.tonnage_load}")

    def unload(self):
        print("\nРазгружаем корабль")

        if self.tonnage_load > 0:
            self.tonnage_load -= 1

        else:
            print("Корабль уже разгружен.")

        print(f"Текущая загруженность корабля {self.tonnage_load}")


warship = WarShip("ZB2", "Калибр")
cargoship = CargoShip("Сухогруз")

print(warship, cargoship)

warship.attack()
warship.sail()

cargoship.sail()
cargoship.load()
cargoship.unload()
