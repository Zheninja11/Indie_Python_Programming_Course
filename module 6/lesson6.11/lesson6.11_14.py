numbers_list = int(input())
lists = [list(map(int, input().split())) for _ in range(numbers_list)]

for i in lists:
    print(len(set(i)))
