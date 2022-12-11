def moos(suur, väike, kogus):
    väikekasutatud = 0
    suurkasutatud = 0
    
    if suur >= kogus // 5:
        suurkasutatud = kogus // 5
    else:
        suurkasutatud = suur
        
    if suurkasutatud*5 != kogus:
        väikekasutatud = kogus-suurkasutatud*5
        if väikekasutatud > väike:
            return -1
    return(väikekasutatud+suurkasutatud)
