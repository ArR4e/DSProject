from random import sample
def bingo():
    while True:
        n = sample(range(1,11),3) + sample(range(11,21),2)
        if not all(x in n for x in [1,2,3]):
            return n
        
    