# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите программу,
# которая выводит их сумму в выходной файл answer.txt.
#
# Пример:
#
# Содержимое файла numbers.txt:
#
# 1
#
# 2
#
# 3
#
# 4
#
# 10
#
# Содержимое файла answer.txt
#
# 20

summ_nums = 0

numbers = open('E:\\task\\numbers.txt', 'r')

for i_line in numbers:
    summ_nums += int(i_line)

amount = open('E:\\task\\summ_amount.txt', 'w')
amount.write(str(summ_nums))

amount.close()
numbers.close()

amount = open('E:\\task\\summ_amount.txt', 'r')

print("Содержимое файла summ_amount.txt")
print(f"\n{amount.read()}")

amount.close()
