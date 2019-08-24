name = input('Enter name:')
print('Hi, ' + name)
seed = len(name)
pi_file = open('pi.txt', 'r')
pi_file.seek(seed)
digit = pi_file.read(1)
guess = input('Enter a single digit guess or "q" to quit: ')
correct = 0
wrong = 0

while guess.lower() != 'q':
    if digit == '.':
        digit = pi_file.read(1)
    elif digit == '\n':
        seed += 1
        pi_file.seek(seed)
    elif guess == digit:
            print('correct!')
            correct += 1
            digit = pi_file.read(1)
    else:
        print('wrong!')
        wrong += 1
    
    guess = input('Enter a single digit guess or "q" to quit: ')

print('Correct :', + correct)
print('Wrong: ', wrong)

pi_file.close()