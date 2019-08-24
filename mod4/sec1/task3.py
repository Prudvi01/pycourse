digits_of_pi_text = open('digits_of_pi.txt', 'r')
pi_digits = digits_of_pi_text.read(4)
print(pi_digits)
option = input('more? (Y or N): ')
while option.lower() != 'n':
    if option.lower() == 'y':
        pi_digits += digits_of_pi_text.read(4)
        print(pi_digits)
        option = input('more? (Y or N): ')

    else:
        print('Invalid')
        option = input('more? (Y or N): ')
 
