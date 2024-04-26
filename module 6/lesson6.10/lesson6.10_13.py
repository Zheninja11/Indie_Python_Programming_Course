colors = [int(color) for color in input().split()]

colors_set = set(colors)

print(len(colors) - len(colors_set))
