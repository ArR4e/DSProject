def erinevad_sümbolid(sõne):
    hulk = set()
    for täht_või_sümbol in sõne:
        hulk.add(täht_või_sümbol)
    return hulk

# print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht_või_sümbol in sõne:
        if täht_või_sümbol in sõnastik:
            sõnastik[täht_või_sümbol] = int(sõnastik[täht_või_sümbol]) + 1
        else:
            sõnastik[täht_või_sümbol] = 1
    return sõnastik

#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    sageduste_sõnastik = sümbolite_sagedus(sõne)
    sõnastik = {}
    täishäälikute_hulk = set()
    kaashäälikute_hulk = set()
    muude_hulk = set()
    for võti in sageduste_sõnastik:
        if võti.lower() in "aeiouõäöü":
            ennik = (võti, sageduste_sõnastik[võti])
            täishäälikute_hulk.add(ennik)
        elif võti.lower() in "bcdfghjklmnpqrsšzžtvwxy":
            ennik = (võti, sageduste_sõnastik[võti])
            kaashäälikute_hulk.add(ennik)
        else:
            ennik = (võti, sageduste_sõnastik[võti])    
            muude_hulk.add(ennik)
    sõnastik["Täishäälikud"] = täishäälikute_hulk
    sõnastik["Kaashäälikud"] = kaashäälikute_hulk
    sõnastik["Muud"] = muude_hulk
    return sõnastik
    
#print(grupeeri("sõida tasa üle silla"))