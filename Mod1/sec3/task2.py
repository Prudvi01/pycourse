first_name = input('First Name:')
new_name = ''
for letter in first_name:
    if letter == 'i' or letter == 'o':
        new_name += letter.upper()
    else:
        new_name += letter

print(new_name)