def erinevad_sümbolid(sõne1):
    tähed = set()
    for täht in sõne1:
        tähed.add(täht)
    return tähed

def sümbolite_sagedus(sõne2):
    sümbolid = {}
    for sümbol in sõne2:
        if sümbol in sümbolid:
            sümbolid[sümbol] = sümbolid[sümbol] + 1
        else:
            sümbolid[sümbol] = 1
    return sümbolid
    
def grupeeri(sõne3):
    märk = sümbolite_sagedus(sõne3)
    võti = märk.keys()
    hulk = {}
    täishäälikud = set()
    kaashäälikud = set()
    muud = set()
    täishäälik = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "õ", "Õ", "ä", "Ä", "ö", "Ö", "ü", "Ü"]
    kaashäälik = ["b", "B", "c", "C", "d", "D", "f", "F", "g", "G", "h", "H", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "p", "P", "q", "Q", "r", "R", "s", "S", "š", "Š", "z", "Z", "ž", "Ž", "t", "T", "v", "V", "w", "W", "x", "X", "y", "Y"]
    for võti in märk:
        if võti in täishäälik:
            täishäälikud.add((võti, märk[võti]))
        elif võti in kaashäälik:
            kaashäälikud.add((võti, märk[võti]))
        elif võti not in täishäälik and võti not in kaashäälik:
            muud.add((võti, märk[võti]))
    hulk["Täishäälikud"] = täishäälikud
    hulk["Kaashäälikud"] = kaashäälikud
    hulk["Muud"] = muud
    return hulk