from random import sample
 
def bingo():
    
    b = sample(range(1, 10), 3)
    if sum(b) == 6:
        b = sample(range(1, 10), 3)
        
    c = sample(range(11, 20), 2)

    a = b + c
    return a

print(bingo())