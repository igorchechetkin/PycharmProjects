# Задача 1. Результаты
# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей.
# Файл первой группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.
#
# Содержимое файла group_1.txt
#
# Бобровский Игорь 10
#
# Дронов Александр 20
#
# Жуков Виктор 30
#
# Содержимое файла group_2.txt
#
# Павленко Геннадий 20
#
# Щербаков Владимир 35
#
# Marley Bob 15
#
# На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы и
# напоследок — произведение очков уже второй группы.
#
# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось,
# этот код просто не работает. Вот что он написал:
#
#
# Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки
# (task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой и также добавьте
# файлы group_1.txt и group_2.txt.


file = open('E:\\task\\group_1.txt', 'r', encoding='Windows-1251')

sum_points = 0

for i_line in file:

    sum_task_list = i_line.split()

    sum_points += int(sum_task_list[2])

file.close()

file = open('E:\\task\\group_1.txt', 'r', encoding='Windows-1251')

diff = 0

for i_line in file:

    dif_task_list = i_line.split()

    diff -= int(dif_task_list[2])

file.close()

file_2 = open('E:\\task\\Additional_info\\group_2.txt', 'r', encoding='Windows-1251')

compose = 0

for i_line in file_2:

    comp_task_list = i_line.split()

    compose *= int(comp_task_list[2])

file_2.close()

print(sum_points)

print(diff)

print(compose)

