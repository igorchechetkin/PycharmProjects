# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие
# «получить урон» (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
#
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
# (а также инкапсуляции и наследования, конечно же).

class Unit:

    def __init__(self, heath):
        self.__heath = heath

    def set_hp(self, amount):
        self.__heath = amount

    def get_hp(self):
        return self.__heath

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - 0)


class Soldier(Unit):

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount)


class Citizen(Unit):

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - (amount * 2))


soldier = Soldier(100)
soldier.get_damage(15)

citizen = Citizen(100)
citizen.get_damage(25)

print(soldier.get_hp())
print(citizen.get_hp())
