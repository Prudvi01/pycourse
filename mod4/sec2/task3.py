cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()

for city in cities_lines:
    if city[0].lower() > 'd':
        print(city)
    
cities_file.close()