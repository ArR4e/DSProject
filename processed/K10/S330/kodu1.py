def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    d = {}
    for sümbol in sõne:
        if sümbol in d:
            d[sümbol] += 1
        else:
            d[sümbol] = 1
    return d

def grupeeri(sõne):
    h1 = set()
    h2 = set()
    h3 = set()
    d = {"Täishäälikud": h1, "Kaashäälikud": h2, "Muud": h3}
    d1 = {}
    for sümbol in sõne:
        if sümbol in d1:
            d1[sümbol] += 1
        else:
            d1[sümbol] = 1
                
    for võti in d1.keys():
        paar = (võti, d1[võti])
        if võti.lower() in ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]:
            h1.add(paar)
        elif võti.lower() in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "š", "z", "ž", "t", "v", "w", "x", "y"]:
            h2.add(paar)
        else:
            h3.add(paar)
    return d