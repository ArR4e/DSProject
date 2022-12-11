def erinevad_sümbolid(sõne) :
    return set(sõne)

def sümbolite_sagedus(sõne) :
    sümbolid = {}
    for el in sõne :
        sümbolid[el] = sõne.count(el)
    return sümbolid

def grupeeri(sõne) :
    täishäälikud = set(['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü'])
    täishäälikute_kogum = {}
    for el in sõne :
        täishäälikute_kogum[el] = sõne.count(el)
    for k in täishäälikute_kogum :
        if täishäälikute_kogum != täishäälikud :
            del täishäälikute_kogum[k]

grupeeri("Hei hopsti, väikevend!")