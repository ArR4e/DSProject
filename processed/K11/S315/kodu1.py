def seosta_lapsed_ja_vanemad (lapsed = 'lapsed.txt', nimed = 'nimed.txt'):
    isikukoodid = []
    nimi = {}
    lapsedjavanemad = {}
    with open (lapsed, 'r', encoding = 'UTF-8') as f:
        for rida in f:
            isikukoodid.append(rida.strip().split())
        
    with open (nimed, 'r', encoding = 'UTF-8') as f:
        for rida in f:
            iknimed = (rida.strip().split())
            isikunimi = ''
            for i in range(len(iknimed)):
                if i > 0:
                    isikunimi += (iknimed[i]+' ')
            nimi[iknimed[0]] = isikunimi.strip()

    for koodid in isikukoodid:
        d = lapsedjavanemad.get(nimi[koodid[1]], set())
        d.add(nimi[koodid[0]])
        lapsedjavanemad[nimi[koodid[1]]] = d
        
    return lapsedjavanemad
    
d = seosta_lapsed_ja_vanemad()

for võti in d:
    print(f"\n{võti}: ", end= '')
    i = 0
    for nimi in d[võti]: 
        if len(d[võti]) == 2:
            if i == 0:
                print(f"{nimi}, ", end= '')
                i += 1
            else:
                print(f"{nimi}", end='')       
        else:
            print(f"{nimi}", end='')
        
