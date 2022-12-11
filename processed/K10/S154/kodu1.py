def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    dictonary = {}
    for täht in sõne:
        dictonary[täht] = dictonary.get(täht, 0) + 1
    return dictonary

def grupeeri(sõne):
    dd = sümbolite_sagedus(sõne)
    ennikud = dd.items()
    d = {}
    täishäälikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaashäälikud = ["h", "j", "l", "m", "n", "r", "s", "v", "k", "p", "t", "g", "b", "d"]
    muud = []
    d['täishäälikud'] = set()
    d['kaashäälikud'] = set()
    d['muud'] = set()
    for märk in sõne:
        if märk in täishäälikud:
            d[märk] = d.get(märk, 0) + 1
            d['täishäälikud'] = (d[märk])
    print(d)
        
    


print(grupeeri("sõida tasa üle silla"))
