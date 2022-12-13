matrix = [[0, 1, 0, 1, 1, 1, 0, 1, 0],
          [1, 0, 0, 1, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 1, 0, 0, 0],
          [1, 1, 1, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 1, 1],
          [1, 0, 0, 0, 0, 0, 1, 0, 1],
          [0, 1, 0, 0, 0, 0, 1, 1, 0]]


username = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


def recommendedfriend(matrix, friend_num): 
    max_recommend = []
    for i in range(len(matrix)):  # O(n)
        count = 0
        for j in range(len(matrix[i])):  #O(n)
            if matrix[friend_num][j] == 1 and matrix[i][j] == 1 and i != friend_num and matrix[i][friend_num] == 0:  #O(1)
                count += 1

        max_recommend.append(count) 
    
    return max_recommend.index(max(max_recommend)) #O(n)
    #O(n) เช็คตอน return max เป็น O(n) แต่ระบบนี้เป็น O(n^2) เพราะข้างในมี loop2 loop ซ้อนกันและเมื่อเราเอาไปคิดมันน้อบกว่า O(n^2) ข้อนี้เลยเป็ฯ O(n^2)

print("Username",username[0]," is recommended", username[recommendedfriend(matrix, 0)])
print("Username",username[1]," is recommended", username[recommendedfriend(matrix, 1)])
print("Username",username[2]," is recommended", username[recommendedfriend(matrix, 2)])
print("Username",username[3]," is recommended", username[recommendedfriend(matrix, 3)])
print("Username",username[4]," is recommended", username[recommendedfriend(matrix, 4)])
print("Username",username[5]," is recommended", username[recommendedfriend(matrix, 5)])
print("Username",username[6]," is recommended", username[recommendedfriend(matrix, 6)])
print("Username",username[7]," is recommended", username[recommendedfriend(matrix, 7)])
print("Username",username[8]," is recommended", username[recommendedfriend(matrix, 8)])
                
                

