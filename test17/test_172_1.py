left_border = int(input('Левая граница: '))
right_border = int(input('Правая граница: '))

cube_list = [number ** 3 for number in range(left_border, right_border + 1)]
square_list = [number ** 2 for number in range(left_border, right_border + 1)]

print(f'\nСписок кубов чисел в диапазоне от {left_border} до {right_border}: {cube_list}')
print(f'Список квадратов чисел в диапазоне от {left_border} до {right_border}: {square_list}')
