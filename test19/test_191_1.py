# Задача 1. Словарь квадратов чисел
# На вход программе поступает целое число num. Напишите программу создания словаря, который включает в себя ключи
# от 1 до num, а значениями соответствующего ключа будет значение ключа в квадрате.
#
# Пример:
#
# Введите целое число: 5
#
# Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

number = int(input('Введите целое число: '))

number_square_dict = dict()

for num in range(1, number + 1):
    number_square_dict[num] = num ** 2

print('\nРезультат: {0}'.format(number_square_dict))
