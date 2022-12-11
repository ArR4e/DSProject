def erinevad_sümbolid(sõne):
    sümbolite_hulk = set(sõne)
    return (sümbolite_hulk)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
        sõnastik[sümbol] = sõnastik.get(sümbol, 0) + 1
    return (sõnastik)

def grupeeri(sõne):
    sõnastik = {}
    täish = {}
    sulgh = {}
    muu = {}
    täishäälikud = ("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
    kaashäälikud = ("k", "p", "t", "g", "b", "d", "s", "c", "f", "h", "j", "l", \
                    "m", "n", "q", "r", "v", "w", "x", "y", "z", "ž", "š")
    for sümbol in sõne:
        if sümbol in täishäälikud:
            täish[sümbol] = täish.get(sümbol, 0) + 1
            sõnastik["Täishäälikud"] = täish
        elif sümbol in kaashäälikud:
            sulgh[sümbol] = sulgh.get(sümbol, 0) + 1
            sõnastik["Kaashäälikud"] = sulgh
        else:
            muu[sümbol] = muu.get(sümbol, 0) + 1
            sõnastik["Muud"] = muu
    return (sõnastik)