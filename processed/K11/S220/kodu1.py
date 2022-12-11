

def seosta_lapsed_ja_vanemad(lapsed, nimedd):
    vanem_laps = {}
    nimed = {}

    f_vanem_laps = open(lapsed)
    for i in f_vanem_laps:
        vanem = i.split()[0]
        laps = i.split()[1]
        if laps not in vanem_laps:
            vanem_laps[laps] = set()
            vanem_laps[laps].add(vanem)
        if laps in vanem_laps :
            vanem_laps[laps].add(vanem)
            
    f_vanem_laps.close()

    f_nimed = open(nimedd)
    for i in f_nimed:
        kood = i.split()[0]
        nimi = i.split()[1] + " " + i.split()[2]
        nimed[kood] = nimi
    f_nimed.close()
    
    uus_vanem_laps = {}
    for i in vanem_laps:
        uus_vanem_laps[i] = set()
        for j in vanem_laps[i]:
            uus_vanem_laps[i].add(nimed[j])
            
    seo = {}
    for i in uus_vanem_laps:
        seo[nimed[i]] = uus_vanem_laps[i]
        
    return seo
        
    
                  
        

seo = (seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))
for i in seo:
        if len(seo[i]) == 2:
            print(i, ":", ",".join(seo[i]))
        elif len(seo[i]) == 1:
            for j in seo[i]:
                print(i, ":", j )

