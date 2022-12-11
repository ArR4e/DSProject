def erinevad_sümbolid(sõne1):
    return set(sõne1)

def sümbolite_sagedus(sõne2):
    sümbolid = erinevad_sümbolid(sõne2)
    sõnastik = {}
    for sümbol in sümbolid:
        väärtus = sõne2.count(sümbol)
        sõnastik[sümbol] = väärtus
    return sõnastik

def grupeeri(sõne3):
    täishäälikud = "aeiouõäöü"
    th = set()
    kaashäälikud = "bcdfghjklmnpqrsšzžtvwxy"
    kh = set()
    muu = set()
    sõnastik1 = sümbolite_sagedus(sõne3)
    sõnastik2 = {}
    for võti in sõnastik1:
        if võti in täishäälikud or võti in täishäälikud.upper():
            th.add((võti, sõnastik1[võti]))
        elif võti in kaashäälikud or võti in kaashäälikud.upper():
            kh.add((võti, sõnastik1[võti]))
        else:
            muu.add((võti, sõnastik1[võti]))
    
    sõnastik2["Täishäälikud"] = th
    sõnastik2["Kaashäälikud"] = kh
    sõnastik2["Muud"] = muu
    
    return sõnastik2