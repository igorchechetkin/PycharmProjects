# Задача 2. Поиск файла 2
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту. Таким образом,
# с ними можно работать точно так же, как и с обычными текстовыми файлами.
#
# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри указанного
# пути все файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).
#
# Подсказка: можно использовать, например, список для сохранения найденного пути.

import os


def find_file(cur_path, file_name):

    for i_elem in os.listdir(cur_path):

        path = os.path.join(cur_path, i_elem)

        if file_name == i_elem:
            print(os.path.abspath(path))
            this_file = open(os.path.abspath(path), 'r', encoding='utf-8')
            for i_string in this_file:
                print(i_string)

        if os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


path_main = input("Ищем в: ")
file = input("Имя файла: ")

print("Найден следующий файл:")
find_file(path_main, file)
