a = int(input())
minimum = 9
maximum = 0
while a > 0:
    last = a % 10
    if last < minimum:
        minimum = last
    if last > maximum:
        maximum = last
    a = a // 10
print(minimum)
print(maximum)
