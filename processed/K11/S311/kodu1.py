def seosta_lapsed_ja_vanemad(lastef, nimedef):
    nimed = {}
    failn = open(nimedef, encoding="UTF-8")
    for rida in failn:
        lahku = rida.split(" ",1)
        nimed[lahku[0]] = lahku[1].strip()
     
    laps_vanema_id = {}
    faill = open(lastef, encoding = "UTF-8")
    for rida in faill:
        lahku = rida.strip().split()
        lapsenimi = nimed[lahku[1]]
        vanemanimi = nimed[lahku[0]]
        if lapsenimi not in laps_vanema_id:
            laps_vanema_id[lapsenimi] = set()
        laps_vanema_id[lapsenimi].add(vanemanimi)
    return laps_vanema_id

laps_vanema_id = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for nimi in laps_vanema_id:
    esimene = True
    print(nimi + ":", end="")
    for vanem in laps_vanema_id[nimi]:
        esimene = False if esimene else print(",", end="")
        print(" " + vanem, end= "")
    print()