fav_food = input("Enter favourite food: ")

for letter in fav_food:
    print(letter)

work_tip = "Good code is commented code"
new_string = ""
for letter in work_tip:
    if letter == " ":
        new_string += "-"
    else:
        new_string += letter

print(new_string)

name = "Hiroto"
print(name[:4])
print(name[1::2])