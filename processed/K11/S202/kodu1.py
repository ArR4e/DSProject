

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f = open(lapsed, encoding="UTF-8")
    ff = open(nimed, encoding="UTF-8")
    võtiisik = {}
    lõppdict = {}
    
    while True:
        rida = ff.readline()
        ridda = rida.strip("\n").split(" ", 1)
        if len(rida) < 2:
            break
        võtiisik[ridda[0]] = ridda[1]
    
    while True:
        RIDA = f.readline()
        RIDDA = RIDA.strip("\n").split(" ")
        if len(RIDA) < 2:
            break
        if võtiisik[RIDDA[1]] not in lõppdict:
            lõppdict[võtiisik[RIDDA[1]]] = set()
            (lõppdict[võtiisik[RIDDA[1]]]).add(võtiisik[RIDDA[0]])
        elif võtiisik[RIDDA[1]] in lõppdict:
            (lõppdict[võtiisik[RIDDA[1]]]).add(võtiisik[RIDDA[0]])
    
    
    
    f.close()
    ff.close()
    return lõppdict

#print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))

