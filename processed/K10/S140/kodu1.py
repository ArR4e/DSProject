def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        sõnastik[i] = sõnastik.get(i, 0) + 1
    return sõnastik

def grupeeri(sõne):
    sagedus = sümbolite_sagedus(sõne)
    täis = ('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü')
    kaas = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
            'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y')
    sõnastik = {"Täishäälikud" : set(), "Kaashäälikud" : set(), "Muud" : set()}
    for täht in sagedus:
        if täht.lower() in täis:
            sõnastik["Täishäälikud"].add((täht, sagedus[täht])
                                         )
        elif täht.lower() in kaas:
            sõnastik["Kaashäälikud"].add((täht, sagedus[täht]))
            
        else:
            sõnastik["Muud"].add((täht, sagedus[täht]))
    return sõnastik
