a = int(input())
b = 1
while b < a:
    b = b + 1
    if a % b == 0:
        break
print(b)
