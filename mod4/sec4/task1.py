file = open('inner_planets.txt', 'w')
file.write('Mercury\nVenus\nEarth\nMars')
file.close()

file = open('inner_planets.txt', 'r')
file_content = file.read()

print(file_content)