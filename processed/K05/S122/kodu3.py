def moos(suur_karp,väike_karp,moosi_kogus):
    läinud = 0
    while moosi_kogus >= 5 and suur_karp >= 1:
        suur_karp = suur_karp - 1
        moosi_kogus = moosi_kogus - 5
        läinud = läinud + 1
    if moosi_kogus == 0:
        return(läinud + moosi_kogus)
    elif väike_karp >= moosi_kogus:
        return (läinud + moosi_kogus)
    else:
        return -1
    