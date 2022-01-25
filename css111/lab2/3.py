# while True:
#     decimal = int(input("please input number : "))
#     param = 999999999
#     str_out = ""
#     while decimal >= 16:
#         hexput = decimal % 16
#         if hexput == 0:
#             str_out = str_out + "0"
#         elif hexput == 1:
#             str_out = str_out + "1"
#         elif hexput == 2:
#             str_out = str_out + "2"
#         elif hexput == 3:
#             str_out = str_out + "3"
#         elif hexput == 4:
#             str_out = str_out + "4"
#         elif hexput == 5:
#             str_out = str_out + "5"
#         elif hexput == 6:
#             str_out = str_out + "6"
#         elif hexput == 7:
#             str_out = str_out + "7"
#         elif hexput == 8:
#             str_out = str_out + "8"
#         elif hexput == 9:
#             str_out = str_out + "9"
#         elif hexput == 10:
#             str_out = str_out + "A"
#         elif hexput == 11:
#             str_out = str_out + "B"
#         elif hexput == 12:
#             str_out = str_out + "C"
#         elif hexput == 13:
#             str_out = str_out + "D"
#         elif hexput == 14:
#             str_out = str_out + "E"
#         elif hexput == 15:
#             str_out = str_out + "F"
#         decimal = decimal // 16
#     str_out = str_out + str(decimal)
#     print("hexdecimal value = ", str_out[::-1])


# while True:
#     num = int(input("please insert number : "))
#     hexe = [0,1,2,3,4,5,6,7,8,9,'A','B','C',"D",'E','F']
#     ans =[]
#     while num >= 16 :
#         result = num%16
#         num = int(num/16)
#         ans.append(hexe[result])
#     ans.append(str(hexe[num]))
#     ans.reverse()
#     print("".join([str(i) for i in ans ]))


# while True:
#     num = int(input("please insert number : "))
#     hexe = "0123456789ABCDEF"
#     ans = ""
#     while num != 0:
#         result = num % 16
#         num = int(num/16)
#         ans = ans + str(hexe[result])
#     print(ans[::-1])


# while True:
#     print(hex(int(input())))


while True: print(hex(int(input())))
