from random import sample

def bingo():
    x = sample(range(1, 11), 3)
    y = sample(range(11, 21), 2)
    if 1 in x and 2 in x and 3 in x:
        bingo()
    else:
        return x+ y
    
    
print(bingo())    
