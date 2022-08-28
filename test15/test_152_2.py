list_numbers = int(input('Кол-во чисел в списке: '))

numbers = []

for number in range(list_numbers):

    print('Введите', number + 1, 'число', end=' ')
    number_count = int(input())

    numbers.append(number_count)

divider = int(input('\nВведите делитель: '))
print()

count = 0
i_amount = 0

for check in numbers:
    count += 1
    if check % divider == 0:
        print('Индекс числа', check, end='')
        print(':', count - 1)
        i_amount += count - 1

print('Сумма индексов:', i_amount)
