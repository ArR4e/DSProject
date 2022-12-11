import random

def bingo():
    a=[]
    a += random.sample(range(1,11),3) + random.sample(range(11,21),2)
    a.sort()
    if a[2] == a[1]+1 == a[0]+2:
        a= bingo()
    return a
print(bingo())