# Lapsed ja Vanemad

def loe_failist(fail):   #Funktsioon failist lugemiseks ja faili ridade panemine sõnastikku
    sõnastik = {}
    f = open(fail, encoding="UTF-8")
    for rida in f:
        elemendid = rida.strip().split(" ")
        sõnastik[elemendid[0]] = " ".join(elemendid[1:])
    f.close()
    return sõnastik

def seosta_lapsed_ja_vanemad(lapsed_fail, nimed_fail):
    lapsed_vanemad = {}  #Tagastatav sõnastik
    isikukoodid = open(lapsed_fail, encoding="UTF-8")   #Avab ainult koodidega faili
    nimed = loe_failist(nimed_fail)   #Paneb nimed ja koodid sõnatsikuks kokku
    #Käib läbi ainult koodidega faili ja seob lapse vanemaga
    for rida in isikukoodid:
        elemendid = rida.strip().split(" ")
        laps = nimed[elemendid[1]]
        vanemad = set()
        if laps in lapsed_vanemad:  #Kontrllib kas laps on juba sõnastikus, kui on siis lisab lapsele teise vanema juurde
            vanem = lapsed_vanemad[laps]
            vanem.add(nimed[elemendid[0]])
            lapsed_vanemad[laps] = vanem
        else:   #Kui laps ei ole sõnastikus, siis ta lisatakse koos 1 vanemaga
            vanemad.add(nimed[elemendid[0]])
            lapsed_vanemad[laps] = vanemad
    isikukoodid.close()

    return lapsed_vanemad

lapsed_vanemad = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
# Tulemuste väljastamine
for i in lapsed_vanemad:
    vanem = ", ".join(e for e in lapsed_vanemad[i])
    print("{0}: {1}".format(i, vanem))

