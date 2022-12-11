laste_fail = "lapsed.txt"
nimede_fail = "nimed.txt"

def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    f_lapsed = open(laste_fail, "r")
    global read_lapsed
    read_lapsed = f_lapsed.readlines()
    f_lapsed.close()
    
    f_nimed = open(nimede_fail, "r")
    global read_nimed
    read_nimed = f_nimed.readlines()
    f_nimed.close()
    sõnastik = {}
    nimekiri = ""
    
    for i in range(erinevad()):
        vanemad = []
        nimed = üksPaar(sõnastik)
        for nimi in nimed[1]:
            vanemad += [nimi]
        vanad = ", ".join(vanemad)
        nimekiri += nimed[0] + ": " + vanad + "\n"
    return nimekiri 

def erinevad():
    hulk = set()
    for rida in read_lapsed:
        jupid = rida.split()
        hulk.add(jupid[1])
    return len(hulk)

def üksPaar(sõnastik):    
    #sõnastik = {}
    luger = 0
    vanemad = set()
    for lapsed in read_lapsed:
        isikukoodid = lapsed.split()
        if luger == 0:
            laps = otsiNimi(isikukoodid[1])
            esimene = isikukoodid[1]
            luger = 1
        if esimene == isikukoodid[1]:
            vanemad.add(otsiNimi(isikukoodid[0]))
            read_lapsed.remove(lapsed)
        sõnastik[laps] = vanemad
    
    return laps, sõnastik[laps]
           

def otsiNimi(isikukood):
  
    for nimi in read_nimed:
        jupid = nimi.split()
        if jupid[0] == isikukood:
            nimi = " ".join(jupid[1:])
            return nimi

print(seosta_lapsed_ja_vanemad(laste_fail, nimede_fail))
            