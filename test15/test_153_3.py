text_list = []
count_words = [0, 0, 0]

for count in range(1, 4):

    print('Введите', count, 'слово: ', end='')
    word = input()

    text_list.append(word)

text_word = ''
print()


while text_word != 'end':

    text_word = input('Слово из текста: ')

    for i in range(3):

        if text_list[i] == text_word:
            count_words[i] += 1


print('\nПодсчёт слов в тексте:')
print(text_list[0], ':', count_words[0])
print(text_list[1], ':', count_words[1])
print(text_list[2], ':', count_words[2])
