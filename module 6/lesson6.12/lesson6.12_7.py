sentence = input().lower().split(',')
words_set = set()

for word in sentence:
    if word not in words_set:
        words_set.add(word)
        print("НЕТ")
    else:
        print("ДА")
