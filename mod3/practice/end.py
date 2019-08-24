def word_mixer(word_list):
    word_list.sort()
    new_words = []

    while len(word_list) > 5:
        rigby = word_list.pop(-5)
        new_words.append(rigby)

        rigby = word_list.pop(0)
        new_words.append(rigby)

        rigby = word_list.pop()
        new_words.append(rigby)
        new_words.append('\n')

    return new_words

entry = input('Enter: ')
word_list = entry.split()
length = len(word_list)

for x in range(length):
    if len(word_list[x]) < 6:
        word_list[x] = word_list[x].lower()
    else:
        word_list[x] = word_list[x].upper()

new_wordss = []
new_wordss = word_mixer(word_list)
print('_______________________________')
for word in range(len(new_wordss)):
    if new_wordss[word] != '\n':
        print(new_wordss[word], end=' ')
    else:
        print(new_wordss[word], end='')
    
