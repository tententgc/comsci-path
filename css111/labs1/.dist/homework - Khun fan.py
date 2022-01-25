try:
    Ex1 = "046750"
    Ex2 = ["421", "666"]
    Ex3 = ["160", "355"]
    Ex4 = "23"
    sum_ans = 0
    a = input("input number of lotto : ")
    if a == Ex1:
        sum_ans += 6000000
    if a[-2:] == Ex4:
        sum_ans += 2000
    for i in range(2):
        if a[:3] == Ex2[i]:
            sum_ans += 4000
        if a[-3:] == Ex3[i]:
            sum_ans += 4000
    if sum_ans > 0:
        print("you lotto prize is " + str(sum_ans), "Bath")
    else:
        print("sorry you are not have money prize")
except:
    print("Please insert number in input !")
