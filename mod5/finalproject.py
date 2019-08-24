def get_names():
    print('list any 5 of the first 20 elements in Periodic table')
    entered = list()
    count = 0
    while count < 5:
        entry = input('Enter the name of an element: ')
        if entry in entered:
            print(entry + ' was already entered')
            entry = input('Enter the name of an element: ')
        elif entry == '':
            entry = input('Enter the name of an element: ')
        else:
            entered.append(entry)
            count += 1
    return entered

    

first20_file = open("C:/pycourse/mod5/elements1_20.txt", 'r')
first20_text = first20_file.readline()
first20_list = []
while first20_text:
    first20_list.append(first20_text.lower().strip())
    first20_text = first20_file.readline()

correct = []
wrong = []

entered_input = get_names()
for entry in entered_input:
    if entry in first20_list:
        correct.append(entry)
    else:
        wrong.append(entry)

print(entered_input)
print(correct)
print(str(len(correct) * 20) + '% correct.')
print('Found: ', end='')
for item in correct:
    print(item.title() + ' ', end='')

print()

print('Not Found: ', end='')
for item in wrong:
    print(item.title() + ' ', end='')
