birthdays = {}

for _ in range(int(input())):
    name, date_month, month  = input().split(' ')

    if month not in birthdays:
        birthdays[month] = [name]
    else:
        birthdays[month].append(name)

for _ in range(int(input())):
    request = input()

    if request in birthdays:
        print(*sorted(birthdays[request]))
    else:
        print('Нет данных')
