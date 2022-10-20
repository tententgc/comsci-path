def num_test(num):
    result = []
    if num[0] > num[1]: #start with >
        for i in range(len(num)-1):
            if i%2 == 0 and num[i] > num[i+1]: #even
                result.append(True)
            elif i%2 != 0 and num[i] < num[i+1]: #odd
                result.append(True)
            else:
                result.append(False)
    elif num[0] < num[1]: #start with <
        for i in range(len(num)-1):
            if i%2 == 0 and num[i] < num[i+1]: #even
                result.append(True)
            elif i%2 != 0 and num[i] > num[i+1]: #odd
                result.append(True)
            else:
                result.append(False)

    return all(result)
    
num = [int(i) for i in list(input())]
print(num_test(num))