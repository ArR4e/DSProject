from random import sample
def bingo():
    arvud = sample(range(1, 11), 3) + sample(range(11, 21), 2)
    while 1 in arvud and 2 in arvud and 3 in arvud:
        arvud = sample(range(1, 11), 3) + sample(range(11, 21), 2)    
    return(arvud)
