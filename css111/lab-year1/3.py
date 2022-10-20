def myreplace(string, old_string, rep_string):
    k = len(old_string)
    count = string.count(old_string)
    while string.count(old_string) > 0:
        for idx in range(len(string)):
            if idx + k > len(string):
                break
            if string[idx : idx + k] == old_string:
                new_string = string[:idx] + rep_string + string[idx + k :]
        string = new_string
    print(new_string)
    print(count)

string = input()
old_string = input()
new_string = input()
myreplace(string, old_string, new_string)