words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 
         'drop', 'produce', 'acquisition', 'cheap', 'strength', 
         'master', 'perception', 'noise', 'strange', 'am']

words_with_position = []
words_with_position_enum = list(enumerate(words, start=1))

for i in words_with_position_enum:
    words_with_position.append(i[::-1])

print(words_with_position)
