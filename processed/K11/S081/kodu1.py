def seosta_lapsed_ja_vanemad(l,n):
    lapsed = open(l, encoding='UTF-8')
    nimed = open(n, encoding='UTF-8')
    
    # laste isikukoodid
    l_i = []
    # vanemate isikukoodid
    v_i = []
    # isikukoodile vastav nimi
    i_n = {}
    # lapsele vastavad vanemad
    l_i_v = {}
    
    # laste ja vanemate iskukukoodide järjendisse lugemine
    for isikukood in lapsed:
        isik = isikukood.strip('\n').split()
        l_i.append(isik[1])
        v_i.append(isik[0])
    
    # iskiukoodile vastav nimi
    for nimi in nimed:
        nimps = nimi.strip('\n').split()
        i_n[nimps[0]] = (nimps[1] + ' ' + nimps[2])
    
    for a in range(len(l_i)):
        indeksid = [i for i, x in enumerate(l_i) if x == l_i[a]]
        vanemad = []
        for s in range(len(indeksid)):
            vanemad.append(i_n[v_i[indeksid[s]]])
        l_i_v[i_n[l_i[a]]] = set(vanemad)
    
    lapsed.close()
    nimed.close()
    print(l_i_v)
    return(l_i_v)
    
    
seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt')    