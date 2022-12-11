from random import sample

def bingo():
    bingo = sample(range(1, 11), 3) + sample(range(11, 21), 2)   
    while sum(bingo[0:3]) == 6:
        bingo = sample(range(1, 11), 3) + sample(range(11, 21), 2)
    else:
        return bingo
    
print(bingo())