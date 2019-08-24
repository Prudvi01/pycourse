long_word = 'juxtaposition'
other_word = ''

for letter in long_word[::2]:
    other_word += letter

print(other_word)

#----------------------------------------------

fav_color = input("Enter favourite color:")
print(fav_color[::-1] + fav_color)