a = int(input())
kvadrat = 0
while 2 ** kvadrat < a:
    kvadrat += 1
if 2 ** kvadrat == a:
    print(kvadrat)
else:
    print("НЕТ")
