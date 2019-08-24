task4_file = open('task4_file.txt', 'w+')
task4_file.write("Line1\nLine2\nLine3\n")
task4_file.close()

task4_file = open('task4_file.txt', 'a+')
for item in range(5):
    task4_file.write('append#' + str(item) + '\n')
    task4_file.seek(0)

task4 = task4_file.read()
print(task4)

