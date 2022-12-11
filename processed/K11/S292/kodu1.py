def seosta_lapsed_ja_vanemad(lapsed, isikud):

    f1 = open(isikud)

    nimed = {}
    for rida in f1:
        andmed = rida.strip().split(" ", 1)
        nimed[andmed[0]] = andmed[1]
        
    f1.close()

    f2 = open(lapsed)

    laps = {}

    for rida in f2:
        andmed = rida.strip().split(" ", 1)
        if nimed[andmed[1]] in laps:
            vanemad = set()
            vanemad.add(laps[nimed[andmed[1]]].pop())
            vanemad.add(nimed[andmed[0]])
            laps[nimed[andmed[1]]] = vanemad
        else:
            laps[nimed[andmed[1]]] = {nimed[andmed[0]]}
               
    f2.close()
    
    return laps