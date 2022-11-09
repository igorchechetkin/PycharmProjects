# Задача 2. Роботы
# На военную базу завезли несколько интересных моделей роботов, которые похожи между собой, но имеют немного
# разные функции. У каждого робота есть номер модели и действие operate, которое означает, что делает робот.
# Особенности роботов следующие:
#
# У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает,
# что он пылесосит пол, и выводит текущую заполняемость мешка.
# У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта
# с помощью этого оружия.
# Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины,
# и при команде operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.
#
# Напишите программу, которая реализует все необходимые классы роботов.

class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"\nМодель робота: {self.model}"


class RobotCleaner(Robot):

    def __init__(self, model):
        super().__init__(model)
        self.bag = 0

    def operate(self):
        print("\nПылесошу пол.")
        self.bag += 1
        print(f"Текущая заполненность пылесборника: {self.bag}")


class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print(f"\nЗащищаю объект с помощью оружия {self.gun}")


class WarUnderwaterRobot(Robot):

    def __init__(self, model, gun, depth):
        super().__init__(model)
        self.gun = gun
        self.depth = depth

    def operate(self):
        print(f"\nЗащищаю объект с помощью оружия {self.gun}")
        print(f"Защищаю под водой на глубине {self.depth}.")


robot_cleaner = RobotCleaner("Белорус")
war_robot = WarRobot("Z22", "Бластер")
war_robot_submarine = WarUnderwaterRobot("Керчь", "Ракета", "1200м")

print(robot_cleaner, war_robot, war_robot_submarine)

robot_cleaner.operate()
war_robot.operate()
war_robot_submarine.operate()
