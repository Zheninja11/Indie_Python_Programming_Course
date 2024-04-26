height_image, width_image = map(int, input().split())
image_source_description = []
negative_image_source = []

for i in range(height_image):
    image_source_description.append(list(input()))

input()

for i in range(height_image):
    negative_image_source.append(list(input()))

number_incorrect_pixels = 0

for i in range(height_image):
    for j in range(width_image):
        if image_source_description[i][j] == negative_image_source[i][j]:
            number_incorrect_pixels += 1
        else:
            continue

print(number_incorrect_pixels)
