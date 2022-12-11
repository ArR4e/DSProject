def seosta_lapsed_ja_vanemad(fail_nimed, fail_lapsed):
    fail_nimed = open('nimed.txt', encoding='utf-8')
    fail_lapsed = open('lapsed.txt',encoding='utf-8')
    
    nimed = {}
    for rida in fail_nimed:
        rida = rida.replace('\n', '').split(' ', 1)
        nimed[rida[0]] = rida[1]

    #failis lapsed - vanem , laps
    koodid = []
    for rida in fail_lapsed:
        rida= rida.replace('\n', '').split(' ')[len(rida)::-1]
        koodid.append(rida)

    lapsed={}
    for n in range(len(koodid)):
        if nimed[koodid[n][0]] not in lapsed:
            lapsed[nimed[koodid[n][0]]] = set()
            lapsed[nimed[koodid[n][0]]].add(nimed[koodid[n][1]])
        else:
            lapsed[nimed[koodid[n][0]]].add(nimed[koodid[n][1]])
    for võti in lapsed:
        if len(lapsed[võti]) == 2:
            võti = list(lapsed[võti])[len(list(lapsed[võti]))::-1]
        
    return lapsed