five_fifteen = []
for item in range(5,16):
    five_fifteen.append(item)
print(five_fifteen) 

spell_list = ['tuesday', 'wednesday', 'february', 'november', 'annual', 'calendar', 'solstice']
for item in range(2,5):
    print(spell_list[item])

print('_________________________')
index = spell_list.index('annual')
for item in range(index,len(spell_list)):
    print(spell_list[item])
