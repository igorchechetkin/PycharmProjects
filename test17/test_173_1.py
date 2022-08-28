# Задача 1. Список чётных чисел
# Пользователь вводит два числа: А и В. Реализуйте код, который генерирует список из чётных чисел в диапазоне от А до B.
# Используйте list comprehensions (как и в следующих задачах).


left_border = int(input('Введите левую границу: '))
right_border = int(input('Введите правую границу '))

list_random = [number for number in range(left_border, right_border + 1) if number % 2 == 0]

print(list_random)