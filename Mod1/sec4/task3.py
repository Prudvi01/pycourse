long_word = "juxtaposition"

first = long_word.find('t')
second = long_word.find('t', first + 1)

print(long_word[first:second])