def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sümbolid = list(sõne)
    sagedused = {}
    for sümbol in sümbolid:
        if sümbol in sagedused:
            sagedused[sümbol] = sagedused[sümbol] + 1
        else:
            sagedused[sümbol] = 1
    return sagedused

def grupeeri(sõne):
    sagedused = sümbolite_sagedus(sõne)
    grupid = {}
    vokaalid = set()
    konsonandid = set()
    muud = set()
    täishäälikud = ["a", "e", "i", "o", "u", "ö", "ä", "õ", "ü"]
    kaashäälikud = ["b", "d", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s",
                    "t", "v", "c", "f", "q", "w", "š", "ž", "z", "x", "y"]
    for el, sagedus in sagedused.items():
        if el.lower() in täishäälikud:
            vokaalid.add((el, sagedus))
        elif el.lower() in kaashäälikud:
            konsonandid.add((el, sagedus))
        else:
            muud.add((el, sagedus))
    grupid["Täishäälikud"] = vokaalid
    grupid["Kaashäälikud"] = konsonandid
    grupid["Muud"] = muud
    return grupid
