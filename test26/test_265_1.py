# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор,
# который также в цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

def counter_gen():

    number = 0
    while True:
        yield number
        number += 1


# my_gen = counter_gen()
# for num in my_gen:
#     print(num)


def gen_prime_numbers(max_nums):
    prime_numbers = []

    for number in range(2, max_nums + 1):

        for prime in prime_numbers:
            if number % prime == 0:
                break

        else:
            prime_numbers.append(number)
            yield number


for i_num in gen_prime_numbers(50):
    print(i_num, end=" ")
