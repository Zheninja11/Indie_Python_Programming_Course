size_table, number_required = map(int, input().split())
table = []

for i in range(1, size_table + 1):
    row = []
    for j in range(1, size_table + 1):
        row.append(i * j)
    table.append(row)

counter_number_required = 0

for i in range(size_table):
    for j in range(size_table):
        if table[i][j] == number_required:
            counter_number_required += 1

print(counter_number_required)
