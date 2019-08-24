purchase_amounts = []

entry = input('Enter')

while entry != 'done':
    purchase_amounts.append(entry)
    entry = input('Enter')

print(purchase_amounts)

subtotal = 0

while purchase_amounts:
    subtotal += float(purchase_amounts.pop())

print(subtotal)
