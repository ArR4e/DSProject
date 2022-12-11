def nimed(fail2):
    t = open(fail2, encoding = "UTF-8")
    
    ni = {}
    for inimene in t:
        inimene = inimene.split()
        inimene[1] += " " + inimene[2]
        ni[inimene[0]] = inimene[1]
    
    t.close()
    return ni

def lapsed(fail1):
    f = open(fail1, encoding = "UTF-8")
    
    lapsed = []
    for isik in f:
        isik = isik.split()
        if isik[1] not in lapsed:
            lapsed.append(isik[1])
        else:
            continue
    f.close()
    return lapsed

def vanemad(laps, fail1, fail2):
    f = open(fail1, encoding = "UTF-8")
    
    nimm = nimed(fail2)
    vanemad = set()
    for appi in f:
        appi = appi.split()
        if appi[1] == laps:
            vanemad.add(nimm[appi[0]])
    
    f.close()
    return vanemad


def seosta_lapsed_ja_vanemad(fail1, fail2):
    la = lapsed(fail1)
    nim = nimed(fail2)
    koos = {}
    for laps in la:
        va = vanemad(laps, fail1, fail2)
        koos[nim[laps]] = va

    return koos

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))