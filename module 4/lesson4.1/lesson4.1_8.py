a, b = map(int, input().split())
number = 0
while a <= b:
    a = a * 3
    b = b * 2
    number = number + 1
print(number)
