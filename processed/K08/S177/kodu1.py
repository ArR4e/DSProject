from random import sample


def bingo():
    while True:
        a=sample(range(1,11),3)
        while 1 in a and 2 in a and 3 in a:
            a=sample(range(1,11),3)
        else:
            break
    
    b=sample(range(11,21),2)
    return (a + b)
        
bingo()