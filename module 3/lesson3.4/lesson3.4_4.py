a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 == a2 == a3:
    print("3")
elif a1 == a2 != a3 or a1 == a3 != a2 or a2 == a3 != a1:
    print("2")
else:
    print("0")
