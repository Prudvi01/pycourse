def footbone(request):
    foot_bones = ['calcaneus', 'talus', 'cuboid', 'navicular', 'lateral cuneiform', 'intermediate cuneiform', 'medial cuneiform']
    
    for bone in foot_bones:
        if request == bone:
            answered.append(bone)
            return 'Correct'           
        else:
            pass
    return 'Incorrect'

answered = []
score = 0
answer = input('Enter: ')
while answer != 'quit':
    if not(answer in answered):
        print(footbone(answer))
        if footbone(answer) == 'Correct':
            score += 1
    else:
        print("Already answered!")
    answer = input('Enter: ')
    

print('Score: ' + str(score))
    