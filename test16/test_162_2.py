quantity_emp = int(input('Кол-во сотрудников: '))

employer_list =[]

for emp_num in range(1, quantity_emp + 1):

    print('Зарплата', emp_num, 'сотрудника:', end=' ')
    employer = int(input(''))
    employer_list.append(employer)

count_emp = 0

for check_zero in employer_list:
    if check_zero == 0:
        employer_list.remove(check_zero)
    count_emp += 1

print('\nОсталось сотрудников:', count_emp)
print('Зарплаты:', employer_list)

print('\nМаксимальная зп:', max(employer_list))
print('Минимальная зп:', min(employer_list))
