n = int(input())
generator_list = [i for i in range(1, n + 1) if n % i == 0]
print(generator_list)
