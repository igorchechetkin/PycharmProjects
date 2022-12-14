# Задача 1. Пунктуация
# Напишите программу, которая считает количество знаков пунктуации в символьной строке.
# К знакам пунктуации относятся символы из набора ".,;:!?". Набор должен храниться в виде множества.
#
# Пример:
#
# Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
#
# Количество знаков пунктуации: 6

import string

text = input('Введите строку: ')

symbol_list = [symbol for symbol in text if symbol in string.punctuation]

symbols = set(symbol_list)

print(symbols)

print(f"\nКоличество знаков пунктуации в строке: {len(symbol_list)}")
