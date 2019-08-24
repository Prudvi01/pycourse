days_file = open('days.txt', 'w+')
days_file.write('Monday\nTuesday\nWednesday\nThursday\nFriday')
days_file.seek(0)
days = days_file.read()
print(days)
print
days_file.seek(0,2)

days_file.write('\nSaturday\nSunday')
days_file.seek(0)
days = days_file.read()
print(days)
days_file.close()