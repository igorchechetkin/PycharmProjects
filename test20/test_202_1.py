import random

some_list_1 = [random.randint(0, 5) for number_1 in range(10)]
some_tuple_1 = tuple(some_list_1)

some_list_2 = [random.randint(-5, 0) for number_2 in range(10)]
some_tuple_2 = tuple(some_list_2)

final_tuple = some_tuple_1 + some_tuple_2

find_elem = final_tuple.count(0)

print(f"Финальный кортеж: {final_tuple}")
print(f"Количество цифр 0 в кортеже: {find_elem}")
