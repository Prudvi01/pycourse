bday_survey = []
day = input('Enter: ')

while day != 'q':
    if int(day) > 0 and int(day) < 32:
        bday_survey.append(day)
    else:
        print('Invalid')
    day = input('Enter: ')

print(bday_survey)