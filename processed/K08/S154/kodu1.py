from random import sample

def bingo():
    m = []
    esimene = sample(range(1, 11), 3)
    if sum(esimene) < 7:
        while sum(esimene) < 7:
            esimene = sample(range(1, 11), 3)
    m += esimene
    teine = sample(range(11, 21), 2)
    m += teine
    return m
    
print(bingo())