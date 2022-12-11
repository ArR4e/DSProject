def erinevad_sümbolid(s):
    eraldi = set(list(s))
    return eraldi

def sümbolite_sagedus(s):
    eraldi = list(s)
    kõik = {}
    for i in eraldi:
        if i in kõik:
            kõik[i] = kõik[i] + 1
        else:
            kõik[i] = 1
    return kõik

def grupeeri(s):
    täishäälikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü", "A", "E", "I", "O", "U", "Õ", "Ä", "Ö", "Ü"]
    kaashäälikud = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "q", "s", "š", "z", "ž", "t", "v", "x", "y", "c", "w", "B", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "Q", "S", "Š", "Z", "Ž", "T", "V", "X", "Y", "C", "W"]
    täish = "Täishäälikud"
    kaash = "Kaashäälikud"
    muuh = "Muud"
    täis = {}
    kaas = {}
    muu = {}
    kõik = {}
    eraldi = list(s)
    for i in eraldi:
# Täishäälikud
        if i in täishäälikud:
            if i in täis:
                täis[i] = täis[i] + 1
            else:
                täis[i] = 1
# Kaashäälikud
        elif i in kaashäälikud:

            if i in kaas:
                kaas[i] = kaas[i] + 1
            else:
                kaas[i] = 1
# Muu
        else:
            if i in muu:
                muu[i] = muu[i] + 1
            else:
                muu[i] = 1
                
    if täish not in kõik:
        kõik[täish] = set(täis.items())
        
    if kaash not in kõik:
        kõik[kaash] = set(kaas.items())

    if muuh not in kõik:
        kõik[muuh] = set(muu.items())
    return kõik

# print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
# print(sümbolite_sagedus("Hei hopsti, väikevend!"))
print(grupeeri("sõida tasa üle silla"))