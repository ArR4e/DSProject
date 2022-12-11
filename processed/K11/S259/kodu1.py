def seosta_lapsed_ja_vanemad(lapsed,nimed):
    lapsed = open(lapsed, 'r')
    nimed = open(nimed, encoding = "utf-8")
    
    isikukoodid = {}
    for rida in lapsed:
        rida = rida.strip()
        i = rida.split(' ')
        if i[1] in isikukoodid:
            isikukoodid[i[1]].append(i[0])
        else:
            isikukoodid[i[1]] = [i[0]]
    lapsed.close()

    seosed = {}
    for rida in nimed:
        rida = rida.strip()
        i = rida.split(' ')
        if i[0] in seosed:
            seosed[i[0]].append(i[1])
        else:
            seosed[i[0]] = i[1] + " " + i[2]
    nimed.close()
    
    lastevanemad = {}
    for i in isikukoodid.keys():
        v_nimed = set()
        for j in isikukoodid[i]:
            v_nimed.add(seosed[j])
        lastevanemad[seosed[i]] = v_nimed
    return lastevanemad
seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")