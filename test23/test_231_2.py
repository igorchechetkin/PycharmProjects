# Задача 2. Возраст
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
#
# Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
# и выводит результат в новый файл result.txt в формате «имя — возраст». Программа должна обрабатывать следующие
# ошибки и выводить сообщение на экран:
#
# 1. Попытка создания файла, который уже существует.
# 2. На чтение ожидался файл, но это оказалась директория.
# 3. Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

ages_file = None
result_file = None

try:

    ages_file = open("ages.txt", "r", encoding="utf-8")
    result_file = open("result.txt", "x", encoding="utf-8")

except (FileExistsError, PermissionError) as exc:

    print("Поймано исключение:", exc, type(exc))


if ages_file and result_file:

    names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    count = 0

    for line in ages_file:

        try:

            clear_line = line.rstrip()
            result_file.write(names[count] + "-" + clear_line + "\n")
            count += 1

        except (ValueError, TypeError) as exc:

            print("Поймано исключение:", exc, type(exc))
