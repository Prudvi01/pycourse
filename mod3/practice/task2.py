for x in range(4):
    print('hello')
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
length = len(spell_list)
print(length)
print('First: ', end='')
for item in range(length//2):
    print(spell_list[item])

print('Second: ', end='')
for item in range(length//2,length):
    print(spell_list[item])

twenties = list(range(20,30))
print(twenties)

total = 0
for num in twenties:
    total += num
print(total)