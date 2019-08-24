random_tip = 'wear a hat when it rains'
print(random_tip.count('e'))
print(random_tip.count('a'))

high = 0
most_freq = ''

for letter in random_tip:
    if random_tip.count(letter) > high and letter.isalpha():
        high = random_tip.count(letter)
        most_freq = letter

print("Most frequent letter is '" + most_freq + "' occuring " + str(high) + " number of times")