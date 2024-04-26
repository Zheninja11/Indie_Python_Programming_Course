n = input()
n1 = input().split()
n2 = len(n1)
for i in range(n2):
    if n in n1[i].lower():
        print(n1[i])
