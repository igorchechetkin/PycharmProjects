# Задача 3. Гистограмма частоты
# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться
# гистограмма частоты букв.
#
# Напишите программу, которая получает сам текст и считает, сколько раз в строке встречается каждый символ.
# На экран нужно вывести содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное значение частоты.
#
# Пример:
#
# Введите текст: Здесь что-то написано
#
#   : 2
#
# - : 1
#
# З : 1
#
# а : 2
#
# д : 1
#
# е : 1
#
# и : 1
#
# н : 2
#
# о : 3
#
# п : 1
#
# с : 2
#
# т : 2
#
# ч : 1
#
# ь : 1
#
# Максимальная частота: 3

def histogram(string):

    histogram_dict = dict()

    for symbol in string:

        if symbol in histogram_dict:
            histogram_dict[symbol] += 1

        else:
            histogram_dict[symbol] = 1

    return histogram_dict


text = input('Введите текст: ').lower()

hist = histogram(text)

for symbol, val in sorted(hist.items()):

    print(f"{symbol} : {val}")

print(f"Максимальная частота: {max(hist.values())}")
