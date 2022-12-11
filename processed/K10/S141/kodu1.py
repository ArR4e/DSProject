def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    #teen järjendi
    jär = []
    for i in sõne:
        jär += i
    d = {}
    #teen sõnastiku
    for sümbol in jär:
        d[sümbol] = d.get(sümbol, 0) + 1
    return d
    
def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    sõnastik1 = sümbolite_sagedus(sõne)

    for sümbol, sagedus in sõnastik1.items():
        if sümbol.lower() in "aeiouõäöü":
            sõnastik["Täishäälikud"].add((sümbol, sagedus))
        elif sümbol.lower() in "bcdfghjklmnpqrsšzžtvwxy":
            sõnastik["Kaashäälikud"].add((sümbol, sagedus))
        else:
            sõnastik["Muud"].add((sümbol, sagedus))
    return (sõnastik)
