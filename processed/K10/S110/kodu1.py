def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    s = {}
    for el in s:
        s['el'] = 1
        väärtus = s[el]
        return väärtus

def grupeeri(sõne):
    s = {}
    s['täishäälik'] = set()
    s['kaashäälik'] = set()
    s['sümbol'] = set()
    for sümbol in s:
        täishäälik = sümbol.lower() in 'aeiouõäöü'
        kaashääik = sümbol.lower() in 'qwrtypsšdfghjklzžxcvbnm'
        sümbolite_sagedus(s)
    for võti in s:
        print(võti)
        print(s[võti])
    return s

print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
print(sümbolite_sagedus("Hei hopsti, väikevend!"))
print(grupeeri("sõida tasa üle silla"))
