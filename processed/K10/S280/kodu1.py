# 1. Teksti analüüs / RP

def erinevad_sümbolid(tekst):
    sümbolid = set()
    for el in tekst:
        if el not in sümbolid:
            sümbolid.add(el)
    return sümbolid

print("hulk ei sisalda kunagi korduvaid elemente")
print()
print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
print()

def sümbolite_sagedus(sõne):
    korras = erinevad_sümbolid(sõne)
    sagedus = {}
    for el in korras:
        palju = sõne.count(el)
        sagedus[el] = palju
    return sagedus
   
print(sümbolite_sagedus("hulk ei sisalda kunagi korduvaid elemente"))
print()

def grupeeri(sõnum):
    täishäälikud = 'AEIOUÕÄÖÜ'
    kaashäälikud = 'VJLMNRSHGKBPDTFZCXYZQW'
    erinevad = sümbolite_sagedus(sõnum)
    täis = set()
    kaas = set()
    muu = set()
    koos = {}
    for el in erinevad:
        if el.upper() in täishäälikud:
            täis.add((el,erinevad[el]))
        elif el.upper() in kaashäälikud:
            kaas.add((el,erinevad[el]))
        else:
            muu.add((el,erinevad[el]))
    koos["Täishäälikud"] = täis
    koos["Kaashäälikud"] = kaas
    koos["Muud"] = muu
    return koos

print(grupeeri("hulk ei sisalda kunagi korduvaid elemente"))    