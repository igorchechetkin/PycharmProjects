# Задача 3. Удаление части
# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B). Напишите программу,
# которая удаляет элементы списка с индексами от А до В. Не используйте дополнительные переменные и методы списков.

import random

original_list = [random.randint(0, 50) for _ in range(30)]
print(original_list)

number_1 = random.randint(0, 10)
number_2 = random.randint(11, 20)
print(number_1, number_2)

original_list[number_1:number_2] = []
print(original_list)
