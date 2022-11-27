# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая эмулирует работу
# цикла for с помощью цикла while и проходит во всем элементам итерируемого объекта. Не забудьте про
# исключение «конца итерации».
from random import randint


def iter_foo(number_list):

    iteration = iter(number_list)

    try:
        while iteration:
            print(next(iteration))

    except StopIteration:
        print("Итератор пуст.")


quantity = int(input("Введите количество чисел: "))
numbers = [randint(-100, 100) for _ in range(quantity)]
iter_foo(numbers)
