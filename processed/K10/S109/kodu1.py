def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for n in sõne:
        if n in sõnastik:
            sõnastik[n] += 1
        else:
            sõnastik[n] = 1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    b = sõnastik["Täishäälikud"] = set()
    a = sõnastik["Kaashäälikud"] = set()
    c = sõnastik["Muud"] = set()
    sõnastik2 = sümbolite_sagedus(sõne)
    for võti in sõnastik2:
        if võti.lower() in "aeiouõäöü":
            b.add((võti, sõnastik2[võti]))
        elif võti.lower() in "bcdfghjklmnpqrstvwxyz":
            a.add((võti, sõnastik2[võti]))
        else:
            c.add((võti, sõnastik2[võti]))

    return sõnastik
