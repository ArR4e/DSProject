

def erinevad_sümbolid(sõne):
    erinevad = set(sõne)
    return erinevad
#print(erinevad_sümbolid("haha1 test 1est"))


def sümbolite_sagedus(ssõne):
    errinevad = set()
    sagedus = {}
    for süm in ssõne:
        if süm in errinevad:
            sagedus[süm] += 1
        else:
            errinevad.add(süm)
            sagedus[süm] = 1
    
    return(sagedus)
#print(sümbolite_sagedus("haha2 test 2est"))

def grupeeri(sssõne):
    gru = {}
    täis = list("aeuioüõöäAEUIOÜÕÖÄ")
    kaas = list("žŽšŠqwrtypsdfghjklxcvbnmQWRTYPSDFGHJKLXCVBNMzZ")
    täishulk = set()
    kaashulk = set()
    muuhulk = set()
    hullhulk = set()
    mitu = {}
    for täht in sssõne:
        if täht in hullhulk:
            mitu[täht] += 1
        else:
            mitu[täht] = 1
            hullhulk.add(täht)
    
    for tähht in sssõne:
        if tähht in täis:
            täishulk.add((tähht, mitu[tähht]))
            
        if tähht in kaas:
            kaashulk.add((tähht, mitu[tähht]))
            
        if not (tähht in täis) and not (tähht in kaas):
            muuhulk.add((tähht, mitu[tähht]))
    
    gru["Täishäälikud"] = täishulk
    gru["Kaashäälikud"] = kaashulk
    gru["Muud"] = muuhulk
    
    return gru

print(grupeeri("sõida tasa üle silla"))
            
            
        
    