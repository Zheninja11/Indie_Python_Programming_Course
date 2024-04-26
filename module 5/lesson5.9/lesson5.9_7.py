a, b = map(int, input().split())
generator_list = []

if a <= b:
    generator_list_if = [i ** 2 for i in range(a, b + 1)]
    generator_list = generator_list_if
elif a > b:
    generator_list_elif = [i ** 3 for i in range(a, b - 1, - 1)]
    generator_list = generator_list_elif

print(generator_list)
