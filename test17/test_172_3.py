def percent_to_up(percent, price):

    return round(price * (1 + percent / 100), 2)


prices = []

for _ in range(5):
    product = float(input('Цена на товар: '))
    prices.append(product)


first_up_price = int(input('Повышение на первый год: '))
second_up_price = int(input('Повышение на второй год: '))

prices_first_up = [percent_to_up(first_up_price, i_price) for i_price in prices]
prices_second_up = [percent_to_up(second_up_price, i_price) for i_price in prices_first_up]

print(f'Сумма цен за каждый год: {round(sum(prices), 2)} {round(sum(prices_first_up), 2)} /'
      f'{round(sum(prices_second_up), 2)}')
