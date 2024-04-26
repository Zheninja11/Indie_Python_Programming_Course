phrase = 'Take only the words that start with t in this sentence'
generator_list = [i for i in phrase.split() if i[0] == 't' or i[0] == 'T']
print(generator_list)
