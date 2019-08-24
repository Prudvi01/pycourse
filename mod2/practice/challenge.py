the_list = ['cat', 'dog', 'machine']

def list_o_matic(the_list, entry):
    if entry == '':
        popped = the_list.pop()
        return popped + ' popped from list'
    elif entry in the_list:
        the_list.remove(entry)
        return '1 instance of "' + entry + '" removed from the list'
    else:
        the_list.append(entry)
        return '1 instance of "' + entry + '" appended to the list'

while the_list:
    print(the_list)
    entry = input('Enter: ')
    if entry == 'quit':
        break
    else:
        print(list_o_matic(the_list, entry))
print('Goodbye!')