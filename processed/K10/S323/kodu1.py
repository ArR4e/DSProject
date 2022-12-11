def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    d = {}
    for sümbol in sõne:
        if sümbol in d:
            d[sümbol] = d[sümbol] + 1
        else:
            d[sümbol] = 1
    return(d)

print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    x = set(sõne)
    taishaalikud = {}
    kaashaalikud = {}
    muu = {}
    t = ["a", "e", "i", "o", "u", "ä", "ü", "ö", "õ"]
    k = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y"]
    
    for sümbol in x:
        kordus = sõne.count(sümbol)
        if sümbol.isalpha() != True:
            muu[sümbol] = kordus
        elif sümbol in t:
            taishaalikud[sümbol] = kordus
        elif sümbol in k:
            kaashaalikud[sümbol] = kordus
    sõnastik = {}
    sõnastik["täishäälikud"] = taishaalikud
    sõnastik["kaashäälikud"] = kaashaalikud
    sõnastik["muu"] = muu
    
    return(sõnastik)
    
print(grupeeri("sõida tasa üle silla"))