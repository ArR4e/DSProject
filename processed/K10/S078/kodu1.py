def erinevad_sümbolid(sõna):
    leitud = set()
    for i in sõna:
        if i not in leitud:
            leitud.add(i)  
    return leitud

def sümbolite_sagedus(sõna):
    leitud = {}
    for el in sõna:
        leitud[el] = leitud.get(el, 0) + 1
    return leitud

def grupeeri(sõna):
    sõnastik = {}
    täishäälikud_hulk = {}
    kaashäälikud_hulk = {}
    muud_hulk = {}
    täishäälikud = 'aeiouõäöüAEIOUÕÄÖÜ'
    kaashäälikud = 'bcdfghjklmnprsšzžtvyqxwBCDFGHJKLMNPRSŠZŽTVYQXW'
    for el in sõna:
        if el in täishäälikud:
            täishäälikud_hulk[el] = täishäälikud_hulk.get(el, 0) + 1
        elif el in kaashäälikud:
            kaashäälikud_hulk[el] = kaashäälikud_hulk.get(el, 0) + 1
        else:
            muud_hulk[el] = muud_hulk.get(el, 0) + 1
    sõnastik['Täishäälikud'] = set(täishäälikud_hulk.items())
    sõnastik['Kaashäälikud'] = set(kaashäälikud_hulk.items())
    sõnastik['Muud'] = set(muud_hulk.items())
    return sõnastik