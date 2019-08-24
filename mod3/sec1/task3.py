paint_color = ['Red', 'Blue', 'Yellow', 'Black', 'White']
color_request = input("Enter: ")
index = ''
for color in paint_color:
    if color_request.lower() == color.lower():
        index = str(paint_color.index(color))
        print('Found at ' + index)