def erinevad_sümbolid(sõne):
    sõnastik = set(sõne)
    return sõnastik

def sümbolite_sagedus(sõne):
    sümbolid = set(sõne)
    sõnastik = {}
    for el in sõne:
        sõnastik[el] = 0
    for el in sõne:
        if el in sümbolid:
            sõnastik[el] += 1
    return sõnastik

def grupeeri(sõne):
    sümbolid = set(sõne)
    täishäälik =  ('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü',
                   'A','E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü')
    kaashäälik = ('q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j',
                  'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
                  'Q', 'W', 'Y', 'Z', 'X', 'K', 'P', 'T', 'G', 'B', 'D', 'H', 'J',
                  'L', 'M', 'N', 'C', 'V', 'R', 'S', 'F')
    märgid = (',', '.', ' ', '!', '"', "'", '?', '-')
    tähed = {}
    for el in sõne:
        tähed[el] = 0
    for el in sõne:
        tähed[el] += 1
    häälikud = {}
    häälikud['Täishäälikud'] = set()
    häälikud['Kaashäälikud'] = set()
    häälikud['Muud'] = set()
    for võti in tähed:
        if võti in täishäälik:
            häälikud['Täishäälikud'].add((võti, tähed[võti]))
        elif võti in kaashäälik:
            häälikud['Kaashäälikud'].add((võti, tähed[võti]))
        elif võti in märgid:
            häälikud['Muud'].add((võti, tähed[võti]))
    return häälikud