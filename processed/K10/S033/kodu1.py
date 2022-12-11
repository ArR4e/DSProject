def erinevad_sümbolid(sõne):
    sümbolid = set(sõne)
    return sümbolid

#print(erinevad_sümbolid('hulk ei sisalda kunagi korduvaid elemente'))

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
        if sümbol in sõnastik:
            sõnastik[sümbol] = sõnastik[sümbol] + 1
        else:
            sõnastik[sümbol] = 1
    return sõnastik

#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    a = ('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', \
         'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü')
    b = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', \
            'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y', \
         'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', \
            'N', 'P', 'Q', 'R', 'S', 'Š', 'Z', 'Ž', 'T', 'V', 'W', 'X', 'Y')
    sõnastik = {}
    kaas = set()
    täis = set()
    muud = set()
    for el in sõne:
        if el in a:
            
            täis.add((el, sõne.count(el)))
        elif el in b:
            kaas.add((el, sõne.count(el)))
        else:
            muud.add((el, sõne.count(el)))
    sõnastik['Täishäälikud'] = täis
    sõnastik['Kaashäälikud'] = kaas
    sõnastik['Muud'] = muud
    return sõnastik

#print(grupeeri("August"))