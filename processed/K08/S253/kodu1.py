from random import sample
def bingo():
    temp = []
    for i in range(4):
        set1 = sample(range(1,11), 3)
        set2 = sample(range(11,21),2)
        temp = set1 + set2
        if not(1 in temp and 2 in temp and 3 in temp):
            break
    
    return temp

print(bingo())