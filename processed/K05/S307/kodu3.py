def moos(suur, väike, moos):
    suurkarp = 0
    väikekarp = 0
    while moos >= 5 and suur > 0:
        moos -= 5
        suurkarp += 1
    if moos == 0:
        return suurkarp
    elif moos - väike > 0:
        return -1
    elif moos > 0:
        while moos > 0:
            moos -= 1
            väikekarp += 1
    return suurkarp + väikekarp
        
        
print(moos(1, 2, 10))