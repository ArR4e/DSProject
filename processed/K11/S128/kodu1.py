#Lapsed ja vanemad

def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    
    f = open(nimede_fail,encoding = "utf-8")
    nimed = {}
    for rida in f:
        andmed = rida.strip().split()
        nimed[andmed[0]] = andmed[1] + " " + andmed[2]
    
    f = open(laste_fail, encoding = "utf-8")
    seos = {}
    for rida in f:
        andmed = rida.strip().split()
        võti = andmed[1] #laps
        vanemad = andmed[0] #vanem
        if võti in nimed.keys():
            võti = nimed[võti]
            if vanemad in nimed.keys():
                vanemad = nimed[vanemad]
        if võti not in seos.keys():
            seos[võti] = set([vanemad])
        else:
            hulk = seos[võti]
            hulk.add(vanemad)
            seos[võti] = hulk
    return seos #võti lapse nimi, väärtus vanemate nimede hulk

lapsed_f = "lapsed.txt"
nimed_f = "nimed.txt"
seosed = seosta_lapsed_ja_vanemad(lapsed_f, nimed_f)
for laps in seosed:
    vanemad = list(seosed[laps])
    if len(vanemad) == 1:
        print(laps + ": " + vanemad[0])
    else:
        print(laps + ": " + vanemad[0] + ", " + vanemad[1])
