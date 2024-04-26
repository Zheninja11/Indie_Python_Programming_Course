x, y = map(int, input().split())
number = 1
while x <= y:
    x = x + (x * 0.15)
    number += 1
print(number)
