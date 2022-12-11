def seosta_lapsed_ja_vanemad(lapsed, nimed):
    nimidict = {}
    lapsjavanem = {}
    vanemlapsnimed = {}
    lapsedf = open(lapsed)
    lapsedfsisu = lapsedf.readlines()
    
    
    for elem in lapsedfsisu:
        isikukood = elem.strip().split()
        vanemset = set()
        if isikukood[1] not in lapsjavanem:
            vanemset.add(isikukood[0])
            lapsjavanem[isikukood[1]] = vanemset
        else:
            vanemsetprev = lapsjavanem.get(isikukood[1])
            vanemsetprev.add(isikukood[0])
            lapsjavanem[isikukood[1]] = vanemsetprev
#     print(lapsjavanem)
    nimedf = open(nimed)
    nimedfsisu = nimedf.readlines()
    for elem in nimedfsisu:
        a = elem.strip().split()
        isikukood = a[0]
        nimi = a[1] + ' ' + a[2]
        nimidict[isikukood] = nimi
#     print(nimidict)
    for vanem in lapsjavanem:
        lapsnimiset = set()
        vanemnimi = nimidict.get(vanem)
        lapsednimi = lapsjavanem[vanem]
        for nimi in lapsednimi:
            lapsnimi = nimidict.get(nimi)
            lapsnimiset.add(lapsnimi)
            lapsnimisetpuhas = str(lapsnimiset).strip("{}").replace("'", "")
#         print(vanemnimi + ': ' + lapsnimisetpuhas)
        vanemlapsnimed[vanemnimi] = lapsnimiset
    lapsedf.close()
    nimedf.close()
    return vanemlapsnimed

    
    
x = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for lapsenimi in x:
    vanemadpuhas = str(x[lapsenimi]).strip('{}').replace("'", "")
    print(lapsenimi + ': ' + vanemadpuhas)

