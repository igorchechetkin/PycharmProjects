def check_film(films, new_film):

    for check in films:

        if check == new_film:

            return True

    return False


films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]
my_film_list = []

while True:

    print('\nВаш текущий топ фильмов:', my_film_list)
    new_film = input('Название фильма: ')

    if check_film(films, new_film):

        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')

        if command == 'добавить':

            for check_f in my_film_list:

                if new_film == check_f:
                    print('Этот фильм уже есть в вашем списке.')
                    my_film_list.remove(check_f)

            my_film_list.append(new_film)

        elif command == 'вставить':
            i_in_list = int(input('На какое место вставляем? '))
            my_film_list.insert(i_in_list, new_film)

        elif command == 'удалить':
            for check_f in my_film_list:
                if new_film == check_f:
                    my_film_list.remove(new_film)

    else:
        print('К сожалению этого фильма нет на нашем сайте :(')


