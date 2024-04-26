year = int(input())

while len(set(str(year + 1))) != 4:
    year += 1

print(year + 1)
