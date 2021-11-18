import random
AvatarNameList = ["Xingqui", "Raiden", "Eula", "Riktor", "Aleister", "Vincent"]
AvatarCount = [0, 0, 0, 0, 0, 0]
for i in range(1, 1001):

    AvatarNumber = random.random()

    if AvatarNumber < 0.1:
        AvatarCount[0] += 1
    elif AvatarNumber < 0.35:
        if random.random() < 0.5:
            AvatarCount[1] += 1
        else:
            AvatarCount[2] += 1
    elif AvatarNumber < 0.65:
        if random.random() < 0.5:
            AvatarCount[3] += 1
        else:
            AvatarCount[4] += 1
    else:
        AvatarCount[5] += 1

    if i % 100 == 0:
        for x in range(6):
            print(f"{AvatarNameList[x]} = {AvatarCount[x]}")
        print(f"summary : {i}")
        print("----------------------------------------------------------------")
