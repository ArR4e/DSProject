lapsed = 'lapsed.txt'
nimed = 'nimed.txt'
def seosta_lapsed_ja_vanemad(lapsed, nimed):
    lapsdict = {}
    f1 = open(lapsed, 'r', encoding = 'utf-8')
    f2 = open(nimed, 'r', encoding = 'utf-8')
    nimidict = {}
    
    for rida in f1:#Seostan isikukoodid
        vanem = set()
        andmed = rida.strip().split()
        vanem.add(andmed[0])
        
        if andmed[1] in lapsdict:
            lapsdict[andmed[1]].add(andmed[0])
        else:
            lapsdict[andmed[1]] = vanem
            
    for rida in f2:#Vahetan sõnastiku võtme, ehk lapse oma, lapse nime vastu
        andmed = rida.strip().split()
        nimi = andmed[1] + ' ' + andmed[2]
        
        for i in lapsdict:
            if andmed[0] == i:
                lapsdict[nimi] = lapsdict[i]
                del lapsdict[i]
        nimidict[andmed[0]] = nimi
    for i in lapsdict:#Vahetan vanemate isikukoodid nende nimede vastu
        pool = set()
        a = 1
        for j in lapsdict[i]:
            if len(lapsdict[i]) == 1:
                pool.add(nimidict[j])
                lapsdict[i] = pool
            elif j in lapsdict[i] and a == 1:
                pool.add(nimidict[j])
                a += 1
                continue
            else:
                pool.add(nimidict[j])
                lapsdict[i] = pool
    f1.close()
    f2.close()

    return lapsdict

print(seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt'))
        
        
