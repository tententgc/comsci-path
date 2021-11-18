import random
AvatarNumber =  random.random()
AvtarName  = ""
if AvatarNumber < 0.1 : AvatarName = "Xingqui"
elif AvatarNumber <0.35 : AvatarName = "Raiden" if random.random()<0.5 else "Eula"
elif AvatarNumber < 0.65 : AvatarName = "Riktor" if random.random() < 0.5 else "Aleister"
else:AvatarName = "Vincent"
print(AvatarName)