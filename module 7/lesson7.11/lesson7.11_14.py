number_unique_commenters = {'Дили': set(), 
                            'Вили': set(), 
                            'Били': set()}

while True:
    row = input()

    if row == 'конец':
        break

    name, comment = row.split(': ')
    number_unique_commenters[name].add(comment)

for name in number_unique_commenters:
    number_unique_commenters[name] = len(number_unique_commenters[name])

for key, value in sorted(number_unique_commenters.items(), key= lambda x: x[1], reverse=True):
    print(f'Количество уникальных комментаторов у {key} - {value}')
