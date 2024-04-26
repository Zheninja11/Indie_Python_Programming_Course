sentence = input()
sentence_set = set(sentence)

for word in sentence:
    if word in sentence_set:
        print(word, end='')
        sentence_set.remove(word)
