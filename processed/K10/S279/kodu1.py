def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
        if sümbol in sõnastik:
            sõnastik[sümbol] = sõnastik[sümbol] + 1
        else:
            sõnastik[sümbol] = 1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    
    sagedus = sümbolite_sagedus(sõne)
    täishäälikud = "aeiouõäöü"
    kaashäälikud = "bcdfghjklmnpqrsšzžtvwxy"
    
    for sümbol in sagedus:
        if sümbol.lower() in täishäälikud:
            sõnastik["Täishäälikud"].add((sümbol, sagedus[sümbol]))
        elif sümbol.lower() in kaashäälikud:
            sõnastik["Kaashäälikud"].add((sümbol, sagedus[sümbol]))
        else:
            sõnastik["Muud"].add((sümbol, sagedus[sümbol]))
    return sõnastik
