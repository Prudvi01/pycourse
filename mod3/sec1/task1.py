birds = ['bird A', 'bird B', 'bird C', 'bird D']

for bird in birds:
    print(bird)

player_points = [2, 3, 4, 5, 6]

for point in player_points:
    print(2 * point)
    
long_string = ''

while birds:
    long_string += birds[0]
    del birds[0]
    if birds:
        long_string += ' '

print(long_string)

    
