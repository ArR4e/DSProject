from random import sample

def bingo():
    while True:
        bingo = []
        bingo += sample(range(1,11),3)
        bingo += sample(range(11,21),2)
        if not (1 in bingo and 2 in bingo and 3 in bingo):
            return bingo
        else:
            continue