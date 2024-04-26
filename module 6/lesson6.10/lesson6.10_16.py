letters = input()

letters_set = {letter for letter in letters if letter.isalpha()} 

print(len(letters_set))
