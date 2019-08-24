days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday']
print(days_of_week)

for i in range(1,6,2):
    print(days_of_week[i])

#----------
phone_letters = [' ', '', 'ABC','DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
print(phone_letters)

day = days_of_week[2]
print(day)

def let_to_num(letter):
    key = 0
    if letter == '':
        return 1

    while key < 10:
        if letter.upper() in phone_letters[key]:
            return key
        else:
            key += 1
    return "Not found"

entry = input('Enter: ')            
print(let_to_num(entry))