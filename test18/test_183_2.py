message = input('Введите текст сообщения: ')

text_list = message.split()

new_message = ' '.join(text_list)

print('\nИсправленный текст:', new_message)
