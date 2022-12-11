from random import sample

def bingo():
    list1 = range(1, 11, 1)
    list2 = range(11, 21, 1)
    
    a = []
    
    while True:
        a = sample(list1, 3)
        _a = a[:]
        _a.sort()
        if _a != [1,2,3]:
            break
        
    b = sample(list2, 2)
    
    return [*a,*b]

print(bingo())
    