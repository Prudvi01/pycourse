matter_states = ['solid', 'liquid', 'gas', 'plasma']
for state in matter_states:
    print(state, end=' - is a state of matter\n')

#________
birds = ['turkey', 'hawk', 'chicken', 'dove', 'crow']
print('Before: ', end='' )
print(birds)

for bird in birds:
    if bird[0].lower() == 'c':
        birds.remove(bird)

print('After: ', end='')
print(birds)

