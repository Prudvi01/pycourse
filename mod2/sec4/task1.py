ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]

print(ft_bones)
index = ft_bones.index('cuboid')

del ft_bones[index]

print(ft_bones)