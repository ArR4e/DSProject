def erinevad_sümbolid(x):
    y = list(x)
    hulk = set(y)
    return hulk

def sümbolite_sagedus(x):
    sõnastik = {}
    for s in set(x):
        b = x.count(s, 0, len(x))
        sõnastik[s] = b
    return sõnastik

def grupeeri(x):
    s6nastik = {}
    s6nastik["Täishäälikud"] = set()
    s6nastik["Kaashäälikud"] = set()
    s6nastik["Muud"] = set()
    for s in set(x):
        if s.lower() in "euioüõaöä":
            b = x.count(s, 0, len(x))
            s6nastik["Täishäälikud"].add((s, b))
        elif s.lower() in "rtpsdfghjklcvbnmwxzqy":
            b = x.count(s, 0, len(x))
            s6nastik["Kaashäälikud"].add((s, b))
        else:
            b = x.count(s, 0, len(x))
            s6nastik["Muud"].add((s, b))
    return s6nastik