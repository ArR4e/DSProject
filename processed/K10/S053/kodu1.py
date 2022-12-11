def erinevad_sümbolid(sõne1):
    tähed = set(sõne1)
    return tähed

def sümbolite_sagedus(sõne2):
    sõnastik = {}
    for arv in sõne2:
        sõnastik[arv] = sõnastik.get(arv, 0) + 1
    return sõnastik

def grupeeri(sõne3):
    täishäälikud = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    kaashäälikud = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'x', 'w', 'y', 'c', 'q']
    sõnastik = {}
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    sagedus = sümbolite_sagedus(sõne3)
    for täht in sagedus.keys():
        if täht.lower() in täishäälikud:
            sõnastik['Täishäälikud'].add((täht, sagedus[täht]))
        elif täht.lower() in kaashäälikud:
            sõnastik['Kaashäälikud'].add((täht, sagedus[täht]))
        else:
            sõnastik['Muud'].add((täht, sagedus[täht]))
    return(sõnastik)