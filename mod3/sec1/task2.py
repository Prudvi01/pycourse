cities = ['New York', 'Shangai', 'Munich', 'Tokyo', 'Dubai', 'Mexico City', 'Sao Paulo', 'Hyderabad']

print('Starting with "m"')
for city in cities:
    if city[0].lower() == 'm':
        print(city)

print('Having "A":')
for city in cities:    
    if 'a' in city:
        print(city)
    
print
print('NOT Having "A":')
for city in cities:    
    if not('a' in city):
        print(city)