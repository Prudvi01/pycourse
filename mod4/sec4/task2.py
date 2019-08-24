outer_planets_file = open('outer_planets.txt', 'w+')
outer_planets_file.write('Jupiter\nSaturn\nUranus\nNeptune')
outer_planets_file.seek(0)
outer_planets = outer_planets_file.read()

print(outer_planets)
outer_planets_file.close()