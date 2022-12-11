from random import sample
def bingo():
    arv=[1,2,3]
    while 3 in arv and 2 in arv and 1 in arv:
            arv=sample(range(1,11), 3)+sample(range(11,21), 2)
    return arv
print(bingo())

    
