n = int(input())
generator_list = [i for i in range(n, n ** 2 + 1) if i % 2 == 1]
print(generator_list)
