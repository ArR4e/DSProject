def erinevad_sümbolid(s):
    return set(s)

def sümbolite_sagedus(s):
    sagedus = {}
    s = list(s)
    for i in s:
        nr = s.count(i)
        sagedus[i] = nr
    return sagedus

def grupeeri(s):
    sagedus = {}
    s = list(s)
    for i in s:
        nr = s.count(i)
        sagedus[i] = nr
    sagedus = list(sagedus.items())
    grupeering = {}
    tais = set()
    kaas = set()
    muu = set()
    for i in sagedus:
        if i[0] in "aeiouõäöüAEIOUÕÄÖÜ":
            tais.add(i)
        elif i[0] in "bdcfghjklmnpqrsšzžtvwxyBDCFGHJKLMNPQRSŠZŽTVWXY":
            kaas.add(i)
        else:
            muu.add(i)
    return {'Täishäälikud':tais, 'Kaashäälikud':kaas, 'Muud':muu}