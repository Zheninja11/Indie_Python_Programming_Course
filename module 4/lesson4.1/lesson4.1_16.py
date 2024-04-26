n = int(input())
while str(n)[0] != '1' and n <= 1000000000:
    a = str(n)[0]
    b = int(a)
    n = n * b
print(n)
