def erinevad_sümbolid(sõne):
    sõne = set(sõne)
    return sõne
print(erinevad_sümbolid("sõida tasa üle silla !"))

def sümbolite_sagedus(sõne):
    sagedus = {}
    for i in set(sõne):
        sagedus[i] = sõne.count(i)
    return sagedus
print(sümbolite_sagedus("sõida tasa üle silla !"))



def grupeeri(sõne):
    sümbolid = erinevad_sümbolid(sõne)
    sagedus = sümbolite_sagedus(sõne)  
    täishääkikud = {"a", "e", "i", "o", "u", "õ", "ä", "ö", "ü",
                    "A", "E", "I", "O", "U", "Õ", "Ä", "Ö", "Ü"}
    kaashälikud = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "z", "t", "v", "w", "x", "y",
                   "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "Z", "T", "V", "W", "X", "Y"}
    täis = set()
    kaas = set()
    muu = set()
    tulemus = {}
    
    for sümbol in sümbolid:
        if sümbol in täishääkikud:
            täis.add((sümbol, sagedus[sümbol]))
            #täis[sümbol] = sagedus[sümbol]
        elif sümbol in kaashälikud:
            kaas.add((sümbol, sagedus[sümbol]))
            #kaas[sümbol] = sagedus[sümbol]
        else:
            muu.add((sümbol, sagedus[sümbol]))
            #muu[sümbol] = sagedus[sümbol]
            
    tulemus["Täishäälikud"] = täis
    tulemus["Kaashäälikud"] = kaas
    tulemus["Muud"] = muu
    return tulemus
   
print(grupeeri("Sõida tasa üle silla"))
    
