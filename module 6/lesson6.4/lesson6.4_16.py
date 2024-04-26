eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = {}

for i in range(len(eng_alphabet)):
    alphabet[eng_alphabet[i]] = i + 1

print(alphabet)
