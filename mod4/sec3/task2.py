rainbow_file = open('rainbow.txt', 'r')
color = rainbow_file.readline()

while color:
    print(color[:-1].upper())
    color = rainbow_file.readline()

rainbow_file.close()