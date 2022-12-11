from random import sample

def bingo():
    
    m = sample(range(1,11),3)
    n = sample(range(11,21), 2)
    global x
    x = m+n
    kt = x[0:3]
    if x[0:3] != [1,2,3]:
        return x
    else:
        bingo()


bingo()
print(x)
