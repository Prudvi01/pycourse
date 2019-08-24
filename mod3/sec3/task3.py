visited_cities = ['New York', 'Shangai Munich', 'Tokyo', 'Dubai', 'Mexico city', 'Hyderabad', 'Sao Paulo']
print(visited_cities)
visited_cities.sort()
print('Sorted list')
print(visited_cities)
print('------')
index = 0
for city in visited_cities:
    print(city[0] + '*')
    if city[0].lower() <= 'q':
        index += 1
    else:
        break

for city in range(index):
    print(visited_cities[city])
    