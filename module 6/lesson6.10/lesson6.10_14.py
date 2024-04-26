from string import ascii_lowercase

text = ascii_lowercase
text_input = input().lower()
text_set = set(text_input)

if len(text) - len(text_set) == 0:
    print("YES")
else:
    print("NO")
