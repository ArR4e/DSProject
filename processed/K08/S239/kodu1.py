from random import sample

def bingo():
    while True:
        bingo=sample(range(1,11),3)
        if sorted(bingo)!=[1,2,3]:
            break
        bingo=[]
    while True:
        a=sample(range(11,21),2)
        bingo=bingo+a
        if sorted(bingo[1:4])!=[1,2,3]:
            break
    return bingo

print(bingo())