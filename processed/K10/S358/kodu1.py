
def erinevad_sümbolid(sone):
    aset = set(sone)
    return aset

def sümbolite_sagedus(sone):
    sone = sone.strip()
    list1 = list(sone)
    sonastik = {}
    for el in list1:
        if el in sonastik:
            sonastik[el] += 1
        else:
            sonastik[el] = 1
    return sonastik

def grupeeri(sone):
    sone = sone.lower().strip()
    list1 = list(sone)
    taishaalikud = {"a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"}
    kaashaalikud = {'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'z', 't', 'v', 'c', 'q', 'w', 'x', 'y'}
    sonastik = {}
    tais = {}
    kaas = {}
    muu = {}
    for el in list1:
        if el in taishaalikud:
            if el in tais:
                tais[el] += 1
            else:
                tais[el] = 1
        elif el in kaashaalikud:
            if el in kaas:
                kaas[el] += 1
            else:
                kaas[el] = 1
        else:
            if el in muu:
                muu[el] += 1
            else:
                muu[el] = 1
    sonastik['Täishäälikud'] = tais
    sonastik['Kaashäälikud'] = kaas
    sonastik['Muud'] = muu
    return sonastik
