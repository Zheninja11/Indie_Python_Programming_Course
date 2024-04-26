offer = input()
a = 'Вопросительное'
b = 'Обычное'
sentence = a if '?' in offer[-1] else b
print(sentence)
