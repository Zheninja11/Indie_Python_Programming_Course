n = int(input())
for i in range(n + 1):
    if i <= 15:
        for j in range(i):
            print(j + 1, end=' ')
        print()
    else:
        break
