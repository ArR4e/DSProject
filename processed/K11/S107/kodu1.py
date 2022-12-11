def seosta_lapsed_ja_vanemad(lapsed, nimed):
    d = {}
    ID_nimi = {}
    laps_vanem = []
    isikukoodid = []
    
    f = open(lapsed, encoding = "utf-8")
    for rida in f:
        osad = rida.strip().split()
        isikukoodid += [[osad[1], osad[0]]]
    f.close()
    
    f2 = open(nimed, encoding = "utf-8")
    for rida in f2:
        osad2 = rida.strip().split()
        ID_nimi[osad2[0]] = osad2[1] + " " + osad2[2]

    f2.close()

    for paar in isikukoodid:
        lapsenimi = ID_nimi.get(paar[0])
        vanemanimi = ID_nimi.get(paar[1])
        laps_vanem += [[lapsenimi, vanemanimi]]
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