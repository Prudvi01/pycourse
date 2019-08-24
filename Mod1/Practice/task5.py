code_tip = "code a conditional decision like you would say it"

print(code_tip.count('i'))

index = code_tip.find('i')
while index != -1:
    print(index)
    index = code_tip.find('i', index + 1)

