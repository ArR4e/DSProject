def erinevad_sümbolid(sõne):
    hulk = set()
    for el in sõne:
        hulk.add(el)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        if el in sõnastik:
            sõnastik[el] +=1
        else:
            sõnastik[el] = 1
    return sõnastik

def grupeeri(sõne):
    sõnastik2 = {}
    täissõnastik = {}
    kaassõnastik = {}
    muusõnastik = {}
    täishäälikud = ("a", "e", "i", "o", "u", "ö", "ä", "ü", "õ")
    kaashäälikud = ("q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m")
    
    for el in sõne:
        if el in täishäälikud:
            täissõnastik[el] += 1
        elif el in kaashäälikud:
            kaassõnastik[el] += 1
        else:
            muusõnastik[el] += 1
    print(täissõnastik)
    print(kaassõnastik)
    print(muusõnastik)
    
    #sõnastik2 = {täissõnastik, kaassõnastik, muusõnastik}

sõne = "Madis"
vastus = erinevad_sümbolid(sõne)
vastus2 = sümbolite_sagedus(sõne)
vastus3 = grupeeri(sõne)
print(vastus)
print(vastus2)
print(vastus3)
        