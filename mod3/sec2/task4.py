word = input("Enter: ")
length = len(word)
odd_letters = []
even_letters = []
for x in range(0,length,2):
    even_letters.append(word[x])
for x in range(1,length,2):
    odd_letters.append(word[x])

print('Even letters: ', end='')
print(even_letters)
print('Odd letters: ', end='')
print(odd_letters)