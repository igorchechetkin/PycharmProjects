import random


def change(nums):
    index = random.randint(0, 4)

    value = random.randint(100, 1000)
    nums_list = list(nums)

    nums_list[index] = value

    return nums_list, value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val_1 = change(my_nums)
new_nums_tuple = tuple(new_nums)

print(f"Первый исправленный кортеж: {new_nums_tuple}\nПервое сгенерированное значение: {rand_val_1}")

new_nums, rand_val_2 = change(new_nums)
new_nums_tuple = tuple(new_nums)

final_val = rand_val_1 + rand_val_2

print(f"\nФинальный кортеж: {new_nums_tuple}\nСумма двух сгенерированных значений: {final_val}")
