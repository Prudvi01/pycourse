cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()

index = 0
for city in cities_lines:
    cities_lines[index] = city[:-1]
    index += 1

for line in cities_lines:
    print(line)