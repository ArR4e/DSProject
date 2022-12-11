import string

def erinevad_sümbolid(sone):
    h1 = set(sone)
    return h1
    
def sümbolite_sagedus(sone):
    sonastik = {}
    for el in erinevad_sümbolid(sone):
        sonastik[el] = sone.count(el)
    return sonastik

def grupeeri(sone):
    t = set()
    k = set()
    m = set()
    alg = sümbolite_sagedus(sone)
    täis = "aeiouõöüä"
    kaas = "qwrtpsdfghjklzxcvbnmžšy"
    muud = string.punctuation
    for el in sone.lower():
        if el in täis:
            t.add((el, alg[el]))
        elif el in kaas:
            k.add((el, alg[el]))
        else:
            m.add((el, alg[el]))

    sonastik = {}
    sonastik["Täishäälikud"] = t
    sonastik["Kaashäälikud"] = k
    sonastik["Muud"] = m
    return sonastik
    

    
print(grupeeri("miks see"))