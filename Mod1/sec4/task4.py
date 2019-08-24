quote = "they stumble who run fast"

space_index = quote.find(" ")

first = 0

while space_index != -1:
    print(quote[first:space_index])
    first = space_index + 1
    space_index = quote.find(" ", space_index + 1)

print(quote[first:])