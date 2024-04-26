countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
country = None
result = False

for key, value in countries.items():
    if city in value:
        country = key
        result = True
    else:
        continue

if result == True:
    print(f'INFO: {city} is a city in {country}')
else:
    print(f'ERROR: Country for {city} not found')
