# Задача 3. Корень диска
# Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт.
# Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.
#
# Результат программы на примере диска G:
#
# Корень диска: G:\\

import os

print("Корень диска:", os.path.abspath('.').split("\\")[0])
