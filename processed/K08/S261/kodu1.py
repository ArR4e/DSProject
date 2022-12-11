from random import sample

def bingo():
    hulk1=sample(range(1,11),3)
    hulk2=sample(range(11,21),2)
    koguhulk=hulk1+hulk2
    if 1 in hulk1 and 2 in hulk1 and 3 in hulk1:
        bingo()
    else:
        return koguhulk
bingo()