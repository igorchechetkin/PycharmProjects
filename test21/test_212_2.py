# Задача 2. Степень числа
# На одном из форумов, посвящённых программированию, пользователь выложил такой код для расчёта степени числа без
# использования циклов, ** и функции math.pow():
#
# def power(a, n):
#
#     return a * power(a, n)
#
# float_num = float(input('Введите вещественное число: '))
#
# int_num = int(input('Введите степень числа: '))
#
# print(float_num, '**', int_num, '=', power(float_num, int_num))
#
# Другие пользователи отметили, что это решение нерабочее и в нём есть ошибки. Исправьте это решение,
# не используя циклы, возведение в степень через ** и функцию math.pow()
#
# Правильный результат:
#
# Введите вещественное число: 1.5
#
# Введите степень числа: 5
#
# 1.5 ** 5 = 7.59375


def power(flo_num, int_num):

    if int_num == 1:
        return flo_num

    num_minus_1 = power(flo_num, int_num - 1)

    return flo_num * num_minus_1


float_num = float(input('Введите вещественное число: '))

int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))
