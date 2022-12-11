def seosta_lapsed_ja_vanemad(lapsed_f,nimed_f):
    f1 = open(lapsed_f,encoding='UTF-8')
    f2 = open(nimed_f,encoding='UTF-8')
    
    nimed = {}
    seostatud={}
    
    for rida in f2:
        korrasta = rida.strip().split(' ',1)
        nimed[korrasta[0]] = korrasta[1]  # nimed[“isikukood”] = “nimi”

    for rida in f1:
        korrasta = rida.strip().split(' ',1)
        vanem = korrasta[0]  # vaja lapsenimi: (vanem1,vanem2)
        laps = korrasta[1]
        lapse_nimi = nimed[laps]
        vanema_nimi = nimed[vanem]
        if lapse_nimi not in seostatud :
            seostatud[lapse_nimi] = set()
            seostatud[lapse_nimi].add(vanema_nimi)
        else:
            seostatud[lapse_nimi].add(vanema_nimi)
        
    return seostatud

sonastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for voti in sonastik:
    print(voti, ':',sonastik[voti])
    
        