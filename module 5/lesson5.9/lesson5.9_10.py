english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
generator_list = [char * (english_alphabet.index(char) + 1) for char in english_alphabet[:n]]
print(generator_list)
