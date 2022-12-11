def erinevad_sümbolid(x):
    hulk = set(x)
    return hulk
def sümbolite_sagedus(y):
    sõnastik = {}
    järjend = []
    for i in y:
        järjend.append(i)
    for a in järjend:
        if a in sõnastik:
            sõnastik[a] = sõnastik[a] + 1
        else:
            sõnastik[a] = 1
    return sõnastik  
def grupeeri(z):
    järjend = []
    sõnastik = {}
    th = set()
    kh = set()
    muud = set()
    täishäälikud = {"a", "e", "i", "o", "u", "ä", "ö", "ü", "õ"}
    kaashäälikud = {"q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"}
    g = sümbolite_sagedus(z)
    for võti in g:
        u = (võti, g[võti])
        järjend.append(u)
    for i in järjend:
        if i[0] in täishäälikud:
            th.add(i)
        elif i[0] in kaashäälikud:
            kh.add(i)
        else:
            muud.add(i)
    sõnastik["Täishäälikud"] = th
    sõnastik["Kaashäälikud"] = kh
    sõnastik["Muud"] = muud
    return sõnastik