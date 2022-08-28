zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(1, 'bear')
zoo.remove('elephant')

i_lion = zoo.index('lion')
i_monkey = zoo.index('monkey')

print('Зоопарк:', zoo)
print('Лев сидит в клетке номер', i_lion + 1)
print('Обезьяна сидит в клетке номер', i_monkey + 1)
