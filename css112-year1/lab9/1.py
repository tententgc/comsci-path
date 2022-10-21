from functools import reduce
def Problem1(atext):
   
    ltext = atext.split(" ")

    anstext=reduce(lambda x,y: x+' '+y, map(lambda x: 'xxx' if x.lower() == 'the' else x, ltext))
    return anstext


atext='The split method is used to split the strings and store them in the list. The built-in method returns a list of the words in the string, using the “delimiter” as the delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.'

print(Problem1(atext))