quote = input("Enter: ")
index = 0 

word = ''
for letter in quote:
    if letter.isalpha():
        word += letter
    else:
        if word != '':
            if word[0].lower() > 'g':
                print(word.upper())
                word = ''
            else:
                word = ''
  
if word != '':
            if word[0].lower() > 'g':
                print(word.upper())
                word = ''