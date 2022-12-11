def moos(suur, väike, kogus):
    kasutatud = 0
    while suur > 0 and kogus - 5 >= 0:
        suur -= 1
        kogus = kogus - 5
        kasutatud += 1
    if väike >= kogus:
        kasutatud += kogus
        return kasutatud
    else:
        return -1
    

    