set_one = set(map(int, input().split()))
set_two = set(map(int, input().split()))

result_set = set_one.difference(set_two)

print(*sorted(result_set))
