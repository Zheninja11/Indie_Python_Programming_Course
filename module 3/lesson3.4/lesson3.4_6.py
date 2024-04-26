age = int(input())
if age > 100:
    print("error")
elif age < 2:
    print("Младенец")
elif 4 > age >= 2:
    print("Малыш")
elif 12 > age >= 4:
    print("Ребенок")
elif 19 > age >= 12:
    print("Подросток")
elif 65 > age >= 19:
    print("Взрослый человек")
elif age >= 65:
    print("Пожилой человек")
