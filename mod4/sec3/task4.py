cities_messy = open('cities_messy.txt', 'r')
line = cities_messy.readline().strip(' :\n')
while line:
    print(line)
    line = cities_messy.readline().strip(' :\n')