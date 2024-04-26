cab_driver_ranking = {}

while True:
    row = input()
    
    if row == 'конец':
        break
    else:
        name, rating = row.split(', ')
        
        if name not in cab_driver_ranking:
           cab_driver_ranking[name] = [int(rating)]
        else:
            cab_driver_ranking[name].append(int(rating))

for driver in cab_driver_ranking:
    cab_driver_ranking[driver] = sum(cab_driver_ranking[driver]) / len(cab_driver_ranking[driver])

cab_driver_ranking= sorted(cab_driver_ranking.items(), key=lambda x: (-x[1], x[0]))

for item in cab_driver_ranking:
    print(f'{item[0]} {item[1]}')
