def seosta_lapsed_ja_vanemad(lastefail,nimefail):
    sonastik=dict()
    nimed=dict()
    #avame nimede faili ja loeme seal andmed nimede sõnastikku
    f_nimed=open(nimefail,encoding="UTF-8")
    for line in f_nimed:
        nimed_loikudeks=line.split(" ",1)
        isikukood=nimed_loikudeks[0]
        nimi=nimed_loikudeks[1]
        nimi_abi=nimi.split("\n")
        nimi_uus=nimi_abi[0]
        nimed[isikukood]=nimi_uus
    #print(nimed)
    f_nimed.close()
    #avame failid
    f_lapsed=open(lastefail,encoding="UTF-8")
        
    for line_lapsed in f_lapsed:
        koodid=line_lapsed.split(" ")
        vanemakood=koodid[0]
        vanemanimi=nimed[vanemakood]
        #print(vanemakood,vanemanimi)
        lapsekood=koodid[1]
        lapsekood_abi=lapsekood.split("\n")
        #print(lapsekood_abi)
        lapsekood_uus=lapsekood_abi[0]
        lapsenimi=nimed[lapsekood_uus]
        #print(lapsekood,lapsenimi)
        if not vanemanimi in sonastik:
            sonastik[vanemanimi]=set()
        sonastik[vanemanimi].add(lapsenimi)    
    f_nimed.close()
    #print(sonastik)
        
    return sonastik

