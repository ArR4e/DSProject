from random import sample
def bingo():
    while True:
        n=sample(range(1,11),3)
        if sorted(n) != [1,2,3]:
            break
    n+=sample(range(11,21), 2)
    
    return n
print(bingo())