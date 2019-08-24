digit_str = '12345678934987654321'
sum = 0
digit_list = list(digit_str)
for x in digit_list:
    sum += int(x)

print('+'.join(digit_list) + ' = ' + str(sum))