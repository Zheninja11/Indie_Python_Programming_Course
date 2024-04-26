a1 = float(input())
a2 = float(input())
a3 = input()
a4 = ['+', '-', '*', '/']
if a3 not in a4:
    print('Неизвестно')
else:
    if a3 == a4[0]:
        print(a1 + a2)
    elif a3 == a4[1]:
        print(a1 - a2)
    elif a3 == a4[2]:
        print(a1 * a2)
    elif a3 == a4[3] and a2 > 0:
        print(a1 / a2)
    elif a3 == a4[3] and a2 == 0:
        print('Неизвестно')
