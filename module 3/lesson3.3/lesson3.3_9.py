a = input().lower()
b = input().lower()
if a[-1] == b[0]:
    print("Good")
else:
    if a[-1] == "ь" and a[-2] == b[0]:
        print("Good")
    else:
        print("Bad")
