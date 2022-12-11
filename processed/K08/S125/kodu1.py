from random import sample

def bingo():
    while True:
        esimesed = sample(range(1,11),3)
        if 1 in esimesed and 2 in esimesed and 3 in esimesed:
            continue
        else:
            break
    
    teised = sample(range(11,21),2)
    bingo = esimesed + teised
    return bingo

print(bingo())