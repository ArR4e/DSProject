# Ülesanne 1 (10. nädal)

def erinevad_sümbolid(sõne):
    täht = set(sõne)
    return tähed

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
        sõnastik[sümbol] = sõnastik.get(sümbol,0)+1
    return sõnastik

def grupeeri(sõne):
    täishäälikud = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    kaashäälikud = ['l', 'm', 'n', 'r', 'v', 'j', 's', 'h', 'g', 'b', 'd', 'k', 'p', 't', 'z', 'f', 'š', 'ž', 'z']
    sõnastik ={}
    täish = set()
    kaash = set()
    muud = set()
    
    for sümbol in sõne:
        sõnastik[sümbol] = sõnastik.get(sümbol,0)+1
        
        for el in sõnastik:
            if el.lower() in täishäälikud and el not in täish:
                täish.add((el,sõnastik[el]))
            elif el.lower() in kaash and el not in kaash:
                kaash.add((el, sõnastik[el]))
            elif el not in muud:
                muud.add((el, sõnastik[el]))
                
        lahendus['täishäälikud'] = täish
        lahendus['kaashäälikud'] = kaash
        lahendus['Muud'] = muud
        
        return lahendus


print(grupeeri('sõida tasa üle silla'))
                