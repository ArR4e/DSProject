def erinevad_sümbolid(sümbolid):
    return set(sümbolid)

def sümbolite_sagedus(sümbolid):
    sõnastik = dict()
    for i in range(len(sümbolid)):
        sõnastik[sümbolid[i]] = sümbolid.count(sümbolid[i])
    return sõnastik

def grupeeri(sümbolid):
    täishäälikud = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    kaashäälikud = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'x', 'y', 'w']
    sõnastik = dict()
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    
    for i in range(len(sümbolid)):
        if sümbolid[i].lower() in täishäälikud:
            grupp = 'Täishäälikud'
        elif sümbolid[i].lower() in kaashäälikud:
            grupp = 'Kaashäälikud'
        else:
            grupp = 'Muud'
        sõnastik[grupp].add((sümbolid[i], sümbolid.count(sümbolid[i])))
    return sõnastik