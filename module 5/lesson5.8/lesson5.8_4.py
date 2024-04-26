number_rows, number_columns = map(int, input().split())
sea_battle = []

sea_battle.append('.' * (number_columns + 2))

for i in range(number_rows):
    sea_battle.append('.' + input() + '.')

sea_battle.append('.' * (number_columns + 2))

counter = 0

for i in range(1, number_rows + 1):
    for j in range(1, number_columns + 1):
        if sea_battle[i][j] == sea_battle[i - 1][j] and sea_battle[i][j] == sea_battle[i + 1][j] and sea_battle[i][j] == sea_battle[i][j + 1] and sea_battle[i][j] == sea_battle[i][j - 1]:
            counter += 1

print(counter)
