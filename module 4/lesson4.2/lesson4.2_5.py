a, b = map(int, input().split())
c = 240 - b # Оставшееся время
d = 0 # Количество решенных задач
e = 0 # Время, потраченное на решение задач
while c >= 0 and e <= c:
    d += 1
    e = e + (d * 5)
if d > a:
    print(a)
else:
    print(d - 1)
