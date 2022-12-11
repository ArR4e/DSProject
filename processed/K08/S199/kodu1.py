from random import sample

def bingo():
    bingonr = []
    
    while True:
        arvud1 = sample(range(1, 11), 3)
        a = arvud1.count(1) + arvud1.count(2) + arvud1.count(3)
        if a == 0 or a == 1:
            bingonr = bingonr + arvud1
            break
        else:
            continue
    arvud2 = sample(range(11, 21), 2)
    bingonr += arvud2
    return(bingonr)

    
    