ip_address = '{0}.{1}.{2}.{3}'

count = 0
numbers = []

while count < 4:

    number_id = int(input('Введите число от 0 до 255: '))

    if 0 <= number_id <= 255:

        numbers.append(number_id)
        count += 1

print(ip_address.format(*numbers))
