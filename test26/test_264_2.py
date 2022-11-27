# Задача 2. Случайная сумма
# Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента
# (первый элемент — просто случайное вещественное число от 0 до 1). Алексею нельзя хранить в памяти
# весь этот список, а со значениями работать как-то надо.
#
# Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу. Также сделайте,
# чтобы при каждом новом вызове итератора в цикле значения считались заново.
#
# Пример работы программы:
#
# Кол-во элементов: 5
#
# Элементы итератора:
#
# 0.74
#
# 1.13
#
# 1.95
#
# 2.2
#
# 2.55
#
# Новое кол-во элементов: 6
#
# Элементы итератора:
#
# 0.79
#
# 1.58
#
# 2.55
#
# 2.81
#
# 3.06
#
# 3.34

from random import uniform


class DataIterator:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        self.first_number = uniform(0, 1)

    def __iter__(self):
        self.first_number = uniform(0, 1)
        return self

    def __next__(self):
        self.counter += 1

        if self.counter > self.limit:
            raise StopIteration()
        self.first_number += uniform(0, 1)

        return round(self.first_number, 2)


ask_quantity = int(input("Кол-во элементов: "))
my_data = DataIterator(ask_quantity)
print("\nЭлементы итератора:")
for element in my_data:
    print(f"\n{element}")

ask_quantity = int(input("Кол-во элементов: "))
my_data = DataIterator(ask_quantity)
print("\nЭлементы итератора:")
for element in my_data:
    print(f"\n{element}")