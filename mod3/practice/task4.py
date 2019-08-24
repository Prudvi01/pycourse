elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
print(elem_1 + elem_2 + elem_3)

jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']
jack_jill.extend(next_line)
print(' '.join(jack_jill))