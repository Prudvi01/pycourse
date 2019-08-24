mean_file = open('mean_temp.txt', 'a+')
mean_file.write('Rio de Janeiro,Brazil,30.0,18.0\n')
mean_file.seek(0)
headings = mean_file.readline().split(',')
city_temp = mean_file.readline()

while city_temp:
    city_list = city_temp.split(',')
    print(headings[0].title() + ' of ' + city_list[0] + ' ' + headings[2] + ' ' + ' is ' + city_list[2] + ' Celsius.')
    city_temp = mean_file.readline()

mean_file.close()