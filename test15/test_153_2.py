line = input('Введите строку: ')
sym_num = int(input('Номер символа: '))

line_list = list(line)

print('\nСимвол слева:', line_list[sym_num - 2])
print('Символ справа:', line_list[sym_num])

for _ in line_list:

    if (line_list[sym_num - 3] == line_list[sym_num - 1]) and (line_list[sym_num - 2] == line_list[sym_num - 1]) \
            or (line_list[sym_num] == line_list[sym_num - 1]) \
            and (line_list[sym_num + 1] == line_list[sym_num - 1]):
        print('\nЕсть ровно два таких же символа.')
        break

    elif (line_list[sym_num - 2] == line_list[sym_num - 1]) or (line_list[sym_num] == line_list[sym_num - 1]):
        print('\nЕсть ровно один такой же символ.')
        break


    else:
        print('Таких же символов нет.')
