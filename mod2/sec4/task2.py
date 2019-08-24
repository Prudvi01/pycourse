ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)

del ft_bones[ft_bones.index('cuboid')]
del ft_bones[ft_bones.index('navicular')]

print(ft_bones)
