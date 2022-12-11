from random import sample

def bingo():
    bingo = []
    
    arv = sample(range(1, 11), 3)
    bingo += arv
    if 1 in bingo and 2 in bingo and 3 in bingo:
        bingo = []
        arv = sample(range(1, 11), 3)
        bingo += arv

    arv = sample(range(11, 21), 2)
    bingo += arv
    return bingo
    
    
print(bingo())