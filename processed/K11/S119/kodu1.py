def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f = open(lapsed)
    l = open(nimed)
    isikukoodid = []
    nimed = []
    isiknimi = {}
    laps = {}
    for rida in f:
        kood = rida.split()
        for el in kood:
            el = int(el)
            isikukoodid.append(el)
    for rida in l:
        nimi = rida.split(" ", 1)
        n = 0
        for i in nimi:
            if n == 1:
                i = i.strip()
            elif n == 0:
                i = int(i)
            nimed.append(i)
            n += 1
    for a in range(0, len(nimed), 2):
        isiknimi[nimed[a]] = nimed[a+1]
    for isik in range(0, len(isikukoodid), 2):
        emaisa = set()
        emaisa.add(isiknimi[isikukoodid[isik]])
        if isiknimi[isikukoodid[isik+1]] in laps:
            laps[isiknimi[isikukoodid[isik+1]]].add(isiknimi[isikukoodid[isik]])
        else:
            laps[isiknimi[isikukoodid[isik+1]]] = emaisa
    return laps
        
           
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")           
        
        
            
    
