rainbow_file = open('rainbow.txt', 'r')
rainbow_colors = rainbow_file.read().split()
rainbow_colors.sort()
for color in rainbow_colors:
    print(color)

rainbow_file.close()
