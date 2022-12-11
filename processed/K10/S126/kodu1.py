def erinevad_sümbolid(sõne):
    sõnehulk = set(sõne)
    return sõnehulk

def sümbolite_sagedus(sõne):
    hulk = {}
    for täht in sõne:
        if täht not in hulk:
            hulk[täht] = 1
        else:
            hulk[täht] += 1
        return hulk
    
print(erinevad_sümbolid(""))
print(sümbolite_sagedus(""))

def grupeeri(sõne):
    täishäälikud = {a, e, i, o, u, õ, ä, ö, ü}
    kaashäälikud = {b, d, f, g, h, j, k, l, m, n, p, r, s, š, z, ž, t, v}
    muud_sümbolid = ",.!?"
    for element in hulk:
        hulk[element] = 0
    else:
        hulk[element] += 1
        return hulk
        
print(grupeeri)