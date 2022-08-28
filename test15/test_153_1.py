line = input('Введите строку: ')

line_list = list(line)
count_change = 0
sym_count = 0

for find_sym in line_list:
    sym_count += 1
    if find_sym == ':':
        line_list[sym_count - 1] = ';'
        count_change += 1


print('Исправленная строка:', end='')

for i in line_list:
    print(i, end='')

print('\nКол-во замен:', count_change)
