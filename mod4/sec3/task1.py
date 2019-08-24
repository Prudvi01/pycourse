rainbow_file = open('rainbow.txt', 'r')
color1 = rainbow_file.readline()
color2 = rainbow_file.readline()
color3 = rainbow_file.readline()

rainbow_file.close()
print(color1)
print(color2)
print(color3)