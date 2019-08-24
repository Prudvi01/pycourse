five_multiples = list(range(5,100,5))
print(five_multiples)
five_multiples.reverse()
print(five_multiples)

fours = list(range(4,44,4))
more_fours = []
more_fours += fours
fours.reverse()
all_num = fours + more_fours
print(all_num)