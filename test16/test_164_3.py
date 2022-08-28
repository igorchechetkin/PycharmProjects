goods = [['яблоки', 50], ['апельсины', 190], ['груши', 100], ['нектарины', 200], ['бананы', 77]]

new_list = []

new_fruit = input('Новый фрукт: ')
price = int(input('Цена: '))

new_list.append(new_fruit)
new_list.append(price)

goods.append(new_list)
print('\nНовый ассортимент:', goods)

i_list = 0

for _ in goods:

    goods[i_list][1] += goods[i_list][1] * 0.08
    i_list += 1

print('\nНовый ассортимент с увел. ценой:', goods)
