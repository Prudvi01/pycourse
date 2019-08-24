first_name = input("Enter your name: ")
new_name = ""

for letter in first_name:
    if letter == 'e' or letter == 't' or letter =='a':
        new_name += '?'
    else:
        new_name += letter

print(new_name[::-1])

topic = ".len(0 returns the length of a string"
print(len(topic))

print(len(topic)//2)

work_tip = "Good code is commented code"

print(work_tip.find("code"))

