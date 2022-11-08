# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом
# (должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов.
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических), а для изменения и получения
# данных объекта напишите специальные геттеры и сеттеры.
#
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами: сеттером и «крайне
# не рекомендуемым», который был показан в уроке.

class Human:

    __count = 0

    def __init__(self):
        self.__name = None
        self.__age = None

    def set_name(self, name):
        if not name.isalpha():
            raise Exception("Имя состоит не только из букв!")
        else:
            self.__name = name
            Human.__count += 1

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age not in range(1, 100):
            raise Exception("Недопустимый возраст!")
        else:
            self.__age = age
            Human.__count += 1

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"Имя: {self.__name}\n" \
               f"Возраст: {self.__age}\n" \
               f"Счетчик: {self.__count}"


human = Human()
human.set_name("Valera")
human.set_age(24)
human.set_age(55)
print(human)
print(Human._Human__count) # Bad idea
