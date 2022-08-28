members= int(input('Кол-во участников: '))
team_membs = int(input('Кол-во человек в команде: '))

team_list =[]
num_mem = 1

if members % team_membs == 0:

    for _ in range(members // team_membs):

        team_list.append(list(range(num_mem, num_mem + team_membs)))
        num_mem += team_membs

    print('\nОбщий список команд:', team_list)

else:
    print()
    print(members, 'участников невозможно поделить на команды по', team_membs, 'человек!')

