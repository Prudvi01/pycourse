rainbow_file = open('rainbow.txt', 'r')
color = rainbow_file.readline()

while color:
    print(color.strip().upper())
    color = rainbow_file.readline()

