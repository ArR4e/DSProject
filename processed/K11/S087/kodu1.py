lapsed = "lapsed.txt"
nimed = "nimed.txt"
def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f1 = open(lapsed, "r", encoding= "utf-8")
    f2 = open(nimed, "r", encoding= "utf-8")
    isikukood = []
    for rida in f1:
        isikukood += [rida.strip()]
    vanemad = []
    for rida2 in f2:
        vanemad += [rida2.strip()]
    vanem = ""
    laps = ""
    for i in isikukood:
        osad = i.split(" ")
        for j in vanemad:
            osad1 = j.split(" ",1)
            if osad[0] in j:
                vanem += osad1[1] + ","
            if osad[1] in j:
                laps += osad1[1] + ","
    f1.close()
    f2.close()
    vanem = vanem.split(",")
    laps = laps.split(",")
    sõnastik = {}
    for i in range(len(laps)):
        asi = set(sõnastik.get(laps[i], []))
        asi.add(vanem[i])
        sõnastik[laps[i]] = asi
    del sõnastik[""]
    return sõnastik
        
    
seosta_lapsed_ja_vanemad(lapsed, nimed)