import math

a, b, c = map(int, input().split())
x = ((a + b) * c) / 8
print(math.ceil(x))
