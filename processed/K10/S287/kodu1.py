sõne = ("Aias sadas saia")
def erinevad_sümbolid(sõne):
    tähed = []
    for i in sõne:
        if not i in tähed:
            tähed.append(i)
        else:
            continue
    return tähed

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        if i in sõnastik:
            sõnastik[i] += 1
        else:
            sõnastik[i] = 1
    return sõnastik
    

def grupeeri(sõne):
    sõnastik["Täishäälikud"] = set()
    sõnastik["Taashäälikud"] = set()
    sõnastik["Muud"] = set()
    kaashäälikud = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, z, t, v, w, x ,y]
    täishäälikud = [a, e, i, o, u, õ, ä, ö, ü]
    sagedus = sümbolite_sagedus(sõne)
    for i in range(len(sagedus)):
        if sagedus[i] in kaashäälikud:
            midagi
        elif sagedus[i] in täishäälikud:
            midagi
        else:
            
    
