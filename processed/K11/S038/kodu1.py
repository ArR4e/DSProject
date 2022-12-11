def seosta_lapsed_ja_vanemad(nimed,lapsed):
    nimed = open("nimed.txt", encoding = "utf-8")
    lapsed = open("lapsed.txt",encoding = "utf-8")
    
    nim = {}
    for rida in nimed:
        rida = rida.replace("\n","").split(" ",1)
        nim[rida[0]] = rida[1]
        
        
    koodid = []
    for rida in lapsed:
        rida = rida.replace("\n","").split(" ")[len(rida)::-1]
        koodid.append(rida)
        
    laps = {}
    for i in range(len(koodid)):
        if nim[koodid[i][0]] not in laps:
            laps[nim[koodid[i][0]]] = set()
            laps[nim[koodid[i][0]]].add(nim[koodid[i][1]])
        else:
            laps[nim[koodid[i][0]]].add(nim[koodid[i][1]])
    for key in laps:
        if len(laps[key]) == 2:
            key = list(laps[key])[len(list(laps[key]))::-1]
            
    return laps

print(seosta_lapsed_ja_vanemad("lapsed.txt","vanemad.txt"))

                                            