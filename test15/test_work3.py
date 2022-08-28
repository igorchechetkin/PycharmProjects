employees = int(input('Кол-во сотрудников в офисе: '))

pass_id_list = []

for _ in range(employees):

    pass_id = int(input('ID сотрудника: '))
    pass_id_list.append(pass_id)


id_check = int(input('Какой ID ищем? '))

for check in pass_id_list:

    if check == id_check:

        print('Сотрудник работает!')
        break

    else:

        print('Сотрудник не работает!')





