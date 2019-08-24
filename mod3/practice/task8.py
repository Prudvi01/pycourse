halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']
code_tip ="Read code aloud or explain the code step by step to a peer"
print(','.join(halogens))
lst_tip = code_tip.split()
print(lst_tip)
for item in range(0,len(lst_tip)):
    lst_tip[item] = lst_tip[item].upper()    
print(''.join(lst_tip))

#_______________________________________
long_word = 'decelerating'
long_list = list(long_word)
for item in long_list:
    print(item)

questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]
for item in questions:
    print(item, end='?\n')

foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]

for item in range(0, len(foot_bones)):
    foot_bones[item] = foot_bones[item].upper()
    print(foot_bones[item], end=', ')

    
