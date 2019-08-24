poem2_messy = open('poem2_messy.txt', 'r')
poem2_lines = poem2_messy.readline().strip('()\n')

while poem2_lines:
    print(poem2_lines.strip('()\n'))
    poem2_lines = poem2_messy.readline()
