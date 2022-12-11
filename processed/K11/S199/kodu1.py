def seosta_lapsed_ja_vanemad(lapsed, nimed):

    laste_fail = open(lapsed)
    nimede_fail = open(nimed)

    nimed = {}
    for rida in nimede_fail:
        kood, nimi = rida.strip().split(" ", 1)
        nimed[kood] = nimi

    lapsed_ja_vanemad = {}
    for rida in laste_fail:
        a, b = rida.strip().split()
        vanem = nimed[a]
        laps = nimed[b]
        if laps in lapsed_ja_vanemad:
            lapsed_ja_vanemad[laps].add(vanem)           
        else:
            lapsed_ja_vanemad[laps] = set()
            lapsed_ja_vanemad[laps].add(vanem)
    
    return(lapsed_ja_vanemad)
        
    laste_fail.close()
    nimede_fail.close()


    

    