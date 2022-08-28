# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком способе шифрования
# каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
#
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и
# сделайте так, чтобы текст был в одном регистре.

def caesar_cipher(string, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in string]

    new_str = ''
    for i_char in char_list:
        new_str += i_char

    return new_str

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

message = input('Введите строку: ').lower()
shift = int(input('Введите сдвиг: '))

cipher = caesar_cipher(message, shift)

print('Зашифрованная строка:', cipher)
