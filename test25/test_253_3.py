# Задача 3. Кастомные исключения
# Исключения в Python также являются классами, и все они берут свои истоки от самого главного класса — Exception.
# И для создания своего собственного класса ошибки достаточно написать его дочерний класс. Например:
#
# class MyOwnException(Exception):
#     pass
#
# raise MyOwnException('Это моя ошибка!')
#
# Причём содержимое объекта исключения чаще всего так и оставляют (просто pass), чтобы не сломать автоматические
# обработчики исключений.
#
# Напишите программу, которая считывает из файла numbers.txt пары чисел, делит первое число на второе и выводит
# ответ на экран. Если первое число меньше второго, то программа выдаёт исключение DivisionError
# (нельзя делить меньшее на большее).
#
# Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.

class DivisionError(Exception):
    pass


def read_and_word_with_file():

    res_list = []

    with open("numbers.txt", "r") as numbers:

        for number in numbers:

            lst = number.rstrip().split()

            try:

                if int(lst[0]) >= int(lst[1]):
                    res_list.append(int(lst[0]) / int(lst[1]))

                else:
                    raise DivisionError

            except DivisionError:
                print("Нельзя делить меньшее на большее")

        return res_list


result_list = read_and_word_with_file()
print(*result_list)
