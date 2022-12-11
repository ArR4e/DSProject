from random import sample

def bingo():
    while True:
        esimesed = sample(range(1,11),3)
        esimesed = sorted(esimesed)
        if esimesed == [1, 2, 3]:
            continue
        else:
            break
    
    teised = sample(range(11,21),2)
    
    kokku = esimesed + teised
    
    return kokku

print(bingo())