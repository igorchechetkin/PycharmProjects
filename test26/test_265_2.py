# Задача 2. Очень большой файл
# Вам на обработку пришёл огромнейший файл с данными. Настолько огромный, что при его открытии компьютер
# просто зависает, так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).
#
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите программу,
# которая подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор.


def read_and_sum_gen():
    nums_list = []
    with open("numbers.txt", "r") as nums_file:

        for number in nums_file:
            nums_list.append(number.rstrip().split(" "))

            for elem in nums_list:

                for num in elem:

                    if num.isdigit():
                        yield int(num)

            nums_list = []


summ = read_and_sum_gen()
result = 0

for i_number in summ:
    result += i_number

print(result)
