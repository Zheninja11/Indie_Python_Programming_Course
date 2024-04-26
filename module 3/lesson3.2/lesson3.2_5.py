a1 = int(input())
a2 = int(input())
minimum = a1 if a1 < a2 else a2
maximum = a2 if a2 > a1 else a1
print(minimum, maximum)
