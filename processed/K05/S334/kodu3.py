from math import floor
def moos(suurkarp, vaikekarp, raskus):
    suur = floor(raskus / 5)
    while suurkarp < suur:
        suur -= 1
    vaike = raskus - suur * 5
    if suur > suurkarp or vaike > vaikekarp:
        return -1
    return vaike + suur    
a = moos(2, 20, 25)
b = moos(2, 6, 14)
c = (1, 2, 10)
