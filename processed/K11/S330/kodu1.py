def seosta_lapsed_ja_vanemad(lapsed, nimed):
    d = {}
    isikukoodid = []
    id_nimi = {}
    laps_vanem = []
    
    f1 = open(lapsed, encoding = "UTF-8")
    for rida in f1:
        osad = rida.strip().split()
        isikukoodid += [[osad[1], osad[0]]]
    f1.close()
  
    f2 = open(nimed, encoding = "UTF-8")
    for rida in f2:
        jupid = rida.strip().split()
        id_nimi[jupid[0]] = jupid[1] + " " + jupid[2]
    f2.close()
    
    for paar in isikukoodid:
        l_nimi = id_nimi.get(paar[0])
        v_nimi = id_nimi.get(paar[1])
        laps_vanem += [[l_nimi, v_nimi]]
    for paar in laps_vanem:
        if paar[0] not in d:
            d[paar[0]] = set()   
        d[paar[0]].add(paar[1])
        
    return d
            
for laps, vanemad in seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").items():
    if len(vanemad) == 2:
        print(laps + ": " + list(vanemad)[0] + ", " + list(vanemad)[1])
    else:
        print(laps + ": " + list(vanemad)[0])