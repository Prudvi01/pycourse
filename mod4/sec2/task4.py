poem2_file = open('poem2.txt', 'r')
poem2_lines = poem2_file.readlines()

index = 0
for line in poem2_lines:
    poem2_lines[index] = line[:-1]
    index += 1

for x in range(-1,-(len(poem2_lines)+1),-1):
    print(poem2_lines[x])

poem2_file.close()