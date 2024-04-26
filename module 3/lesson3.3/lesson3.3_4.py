a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 > a2 and a1 > a3:
    print(a1)
else:
    if a2 > a1 and a2 > a3:
        print(a2)
    else:
        print(a3)
