name = input('Введите имя: ')
order_number = int(input('Номер заказа: '))

string = '\nЗдравствуйте, {user}! Ваш номер заказа: {order}. Приятного дня!'.format(
    user=name,
    order=order_number
)

print(string)
