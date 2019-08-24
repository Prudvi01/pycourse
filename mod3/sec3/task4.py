animals = ['Chimpanzee', 'Panther', 'Wolf', 'Armadillo']
add_animals = []
entry = input('Enter: ')

while entry != 'quit':
    add_animals.append(entry)
    entry = input('Enter: ')

animals.extend(add_animals)
order = input("Alpha or reverse?")
if order.lower() == 'alpha':
    animals.sort()
    print(animals)
elif order.lower() == 'reverse':
    animals.sort()
    animals.reverse()
    print(animals)
else:
    print('Wrong choice!')