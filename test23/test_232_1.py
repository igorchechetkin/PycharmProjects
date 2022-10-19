# Задача 1. Простая программа
# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
# Используйте операторы try except else finally. Обработайте возможные ошибки:
#
# Проблема при открытии файла.
# Нельзя преобразовать данные в целое.
# Неожиданная ошибка.

text = input("Введите любой текст: ")

try:

    new_file = open("new_file.txt", "w", encoding="utf-8")
    new_file.write(text)

except (PermissionError, ValueError, FileExistsError, TypeError) as exc:
    print("Поймано исключение:", exc, type(exc))

else:
    print("Программа отработала без ошибок!")

finally:
    new_file.close()
