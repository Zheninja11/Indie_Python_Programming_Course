def reverse_sequence(sequence):
    if not sequence:
        return []
    else:
        return [sequence[-1]] + reverse_sequence(sequence[:-1])

number = int(input())
numbers = list(map(int, input().split()))

print(*reverse_sequence(numbers))
