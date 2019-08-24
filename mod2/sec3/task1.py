def str_replace(int_list, index):
    for i in index:
        if int_list[i] < 5:
            int_list[i] = 'small'
        elif int_list[i] > 5:
            int_list[i] = 'large'
    return int_list

three_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = [0, 8, 6]
print(three_num)
print(str_replace(three_num, index))

