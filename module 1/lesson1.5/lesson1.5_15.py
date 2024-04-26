a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = a1 * a2 * a3
b2 = a1 + a2 + a3
b3 = a1 * (a2 + a3)
b4 = a1 + (a2 * a3)
b5 = (a1 * a2) + a3
b6 = (a1 + a2) * a3
print(max(b1, b2, b3, b4, b5, b6))