#Seosta lapsed ja vanemad
def seosta_lapsed_ja_vanemad(lapsed,nimed):
    #Failid
    laps = open("lapsed.txt", "r", encoding = "UTF-8")
    nimi = open("nimed.txt" , "r", encoding = "UTF-8")
    #Paarid {lapsed ja vanemad}, isikukoodi (nr), nimed {nr ja nimi}
    paarid = {}
    lapsed = set()
    nimed = {}
    #Isikukoodid
    for rida in laps:
        ik = rida.strip().split(" ")
        lapsed.add((ik[0],ik[1]))
    #Isikukoodid ja nimed 
    for rida in nimi:
        ikn = rida.strip().split(" ")
        nimed[ikn[0]] = ikn[1] + " " + ikn[2]
    laps.close
    nimi.close
    #Paaride tekitamine
    for kood, nimi in nimed.items():
        vanemad = set()
        for vanemIK, lapsIK in lapsed:
            if kood ==lapsIK:
                vanemad.add(nimed[vanemIK])
        if len(vanemad) > 0:
            paarid[nimi] = vanemad
    #Paaride tagastamine 
    return paarid    