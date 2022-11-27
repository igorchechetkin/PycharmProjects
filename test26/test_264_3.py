# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
#
# Основной код:
#
# prime_nums = Primes(50)
#
# for i_elem in prime_nums:
#
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
#
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

class Primes:

    def __init__(self, max_qua):
        self.max_qua = max_qua
        self.number = 1
        self.prime_list = []

    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        while self.number <= self.max_qua:
            self.number += 1

            for prime in self.prime_list:

                if self.number % prime == 0:
                    break

            else:
                self.prime_list.append(self.number)
                return self.number

        raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:

    print(i_elem, end=' ')
