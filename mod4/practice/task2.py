mean_temp_file = open('mean_temp.txt', 'r')
headings = mean_temp_file.readline()
print(headings)
headings_list = headings.split(',')
print(headings_list)
city_temp = mean_temp_file.readline()
while city_temp:
    city_list = city_temp.split(',')
    print(city_list[0] + "'s highest average temperature is " + city_list[2])
    city_temp = mean_temp_file.readline()
    
mean_temp_file.close()