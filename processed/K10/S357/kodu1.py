def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    tähed = set(sõne)
    
    for täht in tähed:
        sõnastik[täht] = 0
    
    for a in sõne:
        if a in tähed:
            sõnastik[a] += 1
    
    return sõnastik

def grupeeri(sõne):
    tähed = sümbolite_sagedus(sõne)
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    
    for el in tähed:
        if str(el).lower() in ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]:
            sõnastik["Täishäälikud"].add((el, tähed[el]))
        elif str(el).lower() in ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "y"]:
            sõnastik["Kaashäälikud"].add((el, tähed[el]))
        else:
            sõnastik["Muud"].add((el, tähed[el]))
    return sõnastik