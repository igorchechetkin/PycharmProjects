# Задача 3. Универсальная программа
# Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
# При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
#
# Напишите функцию, которая возвращает список из элементов итерируемого объекта
# (кортежа, строки, списка, словаря), у которых индекс чётный.
#
# Пример 1:
#
# Допустим, есть такая строка: 'О Дивный Новый мир!'
#
# Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']
#
# Пример 2:
#
# Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
#
# Результат: [100, 300, 0, 'а']
#
# Примечание: для проверки типа можно использовать функцию
#
# isinstance(<элемент>, <тип данных>), которая возвращает True, если элемент принадлежит к этому типу данных,
# и возвращает False в противном случае.

from collections.abc import Iterable


def even_indexes(data):

    result_list = [symbol for (i_sym, symbol) in enumerate(data) if i_sym % 2 == 0]

    return result_list


some_data = 'О Дивный Новый мир!'

if isinstance(some_data, Iterable):
    final_list = even_indexes(some_data)
    print(f"\nРезультат: {final_list}")

else:
    print("Ошибка типа данных! Они не итерируемы.")
