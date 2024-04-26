a1, a2, a3 = map(int, input().split())
if a1 > a2 > a3:
    print(a1 - a3)
else:
    if a2 > a1 > a3:
        print(a2 - a3)
    else:
        if a2 > a3 > a1:
            print(a2 - a1)
        else:
            if a3 > a1 > a2:
                print(a3 - a2)
            else:
                if a3 > a2 > a1:
                    print(a3 - a1)
                else:
                    print(a1 - a2)
