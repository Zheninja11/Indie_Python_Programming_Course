import json

alphabet = {}

for i in range(26):
    alphabet[chr(97+i)] = i+1

json_data = json.dumps(alphabet)

print(json_data)
