dogs = int(input('Сколько собак? '))

dogs_point = []

for dog in range(dogs):

    print('Собака', dog + 1, end='')
    print(', очки =', end=' ')

    points = int(input(''))
    dogs_point.append(points)

print('\nБаговая таблица:', dogs_point)

maximum = dogs_point[0]
minimum = dogs_point[0]


for check in dogs_point:

    if maximum < check:
        maximum = check

    elif minimum > check:
        minimum = check

for count in range(dogs):

    if dogs_point[count] == maximum:
        dogs_point[count] = minimum

    elif dogs_point[count] == minimum:
        dogs_point[count] = maximum

print('\nИсправленная таблица:', dogs_point)
