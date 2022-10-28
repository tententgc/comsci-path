x = [ord(i) for i in input() if i.isalpha()]
#เน้นไว BigO น้อยด้วย quicksort
def quicksort(x): 
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

x = quicksort(x)
print("".join( [chr(i) for i in x]))
