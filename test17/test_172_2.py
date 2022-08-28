line = input('Введите строку: ')
symbol = input('Введите дополнительный символ:')

double_letter_list = [letter * 2 for letter in line]
gluing_with_symbol = [symbols + symbol for symbols in double_letter_list]

print(f'\nСписок удвоенных символов: {double_letter_list}')
print(f'Склейка с дополнительным символом: {gluing_with_symbol}')
