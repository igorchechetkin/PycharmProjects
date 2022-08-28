words_list = [input('Введите слово: ') for _ in range(3)]

text = input('Введите текст: ')

count_word = [text.count(word) for word in words_list]

print(sum(count_word))
