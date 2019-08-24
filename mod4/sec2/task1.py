cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()

for city in cities_lines:
    print(city)
