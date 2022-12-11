from random import sample

def bingo():
    esimesed = sample(range(1,11),3)
    
    while sum(esimesed) == 6:
        esimesed = sample(range(1,11),3)
        
    
    teised = sample(range(11,21),2)
    kokku = esimesed + teised
    return kokku

print(bingo())