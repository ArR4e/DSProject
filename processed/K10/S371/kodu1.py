def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
        sõnastik[sümbol] = sõnastik.get(sümbol, 0) + 1
    return sõnastik
    
print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    täishäälikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaashäälikud = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "š", "z", "ž", "t", "v", "w", "x", "y"]
    sõnastik = {}
    grupeeritud = {}
    täishäälikute_hulk = set()
    kaashäälikute_hulk = set()
    sümbolite_hulk = set()
    
    for sümbol in sõne:
        sõnastik[sümbol] = sõnastik.get(sümbol, 0) + 1
    
    for sümbol in sõnastik:
        if sümbol.lower() in täishäälikud and sümbol not in täishäälikute_hulk:
            täishäälikute_hulk.add((sümbol, sõnastik[sümbol]))
        elif sümbol.lower() in kaashäälikud and sümbol not in kaashäälikute_hulk:
            kaashäälikute_hulk.add((sümbol, sõnastik[sümbol]))
        elif sümbol not in sümbolite_hulk:
            sümbolite_hulk.add((sümbol, sõnastik[sümbol]))
    
    grupeeritud["Täishäälikud"] = täishäälikute_hulk
    grupeeritud["Kaashäälikud"] = kaashäälikute_hulk
    grupeeritud["Muud"] = sümbolite_hulk
    
    return grupeeritud

print(grupeeri("sõida tasa üle silla"))