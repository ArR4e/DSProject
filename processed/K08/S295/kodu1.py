from random import sample
#[]
def bingo():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = [11,12,13,14,15,16,17,18,19,20]
    a = sample(list1,3)
    b = sample(list2,2)
    while True:
        a.sort()
        if a != [1,2,3]:
            break
        else:
            a = sample(list1,3)
    return(a+b)
    
bingo()