a = int(input())
b = list(map(int, input().split()))
count = [0] * 201
for i in b:
    count[i] += 1
for i in range(-100, 101):
    if count[i] > 0:
        print((str(i) + " ") * count[i], end="")
