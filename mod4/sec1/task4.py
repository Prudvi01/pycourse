cities_file = open('cities.txt', 'r')
cities = cities_file.read()
initials = ''
for x in cities:
    if x.isupper() or x == '\n':
        initials += x

print(initials)
        
