def letters_count(message):
    count = 0

    for letters_count in message:
        count += 1

    return count


first_mess = input('Первое сообщение: ')
second_mess = input('Второе сообщение: ')

count_f = letters_count(first_mess)
count_s = letters_count(second_mess)

third_mess = ''

if count_f > count_s:
    third_mess = first_mess + ' ' + second_mess

elif count_s > count_f:
    third_mess = second_mess + ' ' + first_mess

else:
    third_mess = 'Ой'

print('\nТретье сообщение:', third_mess)

