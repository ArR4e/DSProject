def seosta_lapsed_ja_vanemad(koodid, nimedega):
    isikukoodid = open(koodid, encoding = "UTF=8")
    
    välja = {}
    for i in isikukoodid:
        hulk = set()

        sisu = i.strip().split(" ")
        vanema = sisu[0]
        lapse = sisu[1]
        with open(nimedega, encoding ="UTF-8") as nimed:
            for l in nimed:
                seest = l.strip().split(" ")
                isikukood = seest[0]
                nimi = seest[1] + " " + seest[2]
                if lapse == isikukood:
                    if lapse not in välja:
                        välja[nimi] = 
                        
                    else:
                        välja[nimi] += välja[nimi]
            
# kahjuks ei osanud siit edasi teha

    for m in välja:
        nimed = open(nimedega, encoding ="UTF-8")
        sisu = nimed.readline()
        uuest = m.strip().split(" ")
        if isikukood in l:
            hulk.add(nimi)
            
    isikukoodid.close()

    return välja


print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))