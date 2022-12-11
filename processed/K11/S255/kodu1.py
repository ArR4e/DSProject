def seosta_lapsed_ja_vanemad(nimedtxt, lapsedtxt):
    nimed = {}
    mida_tahame = {}
    #nimed
    with open(nimedtxt, 'r', encoding='UTF-8') as ava_fail:
        for i in ava_fail:
            a = (i.strip()).split()
            nimed[a[0]] = a[1] + ' ' + a[2]
        a = []
    #vanemad
    with open(lapsedtxt, 'r', encoding='UTF-8') as ava_fail2:
        for j in ava_fail2:
            a = (j.strip()).split()
            vanem = a[0]
            laps = a[1]
            mida_tahame[nimed[laps]] = set()
            
            mida_tahame[nimed[laps]].add(nimed[vanem])
            if nimed[vanem] not in mida_tahame:
                mida_tahame[nimed[laps]].add(nimed[vanem])
        print(mida_tahame)
        
seosta_lapsed_ja_vanemad('nimed.txt', 'lapsed.txt')