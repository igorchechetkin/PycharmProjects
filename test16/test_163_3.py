pack_quantity = int(input('Кол-во пакетов: '))

packs = []
decode = []

lost_packs = 0

for pack in range(pack_quantity):

    print('\nПакет номер', pack + 1)

    for count_bit in range(4):

        print(count_bit + 1, 'бит:', end=' ')
        bit = int(input(''))
        packs.append(bit)

    if packs.count(-1) <= 1:

        decode.extend(packs)

    else:

        print('Много ошибок в пакете.')
        lost_packs += 1

    packs = []

errors_dec = decode.count(-1)

print('\nПолученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', errors_dec)
print('Кол-во потерянных пакетов:', lost_packs)
