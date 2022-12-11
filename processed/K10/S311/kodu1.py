def erinevad_sümbolid(sag):
    return set(sag)

def sümbolite_sagedus(sag):
    sõnastik = {}
    for i in sag:
        if i not in sõnastik:
            sõnastik[i] = 1
        else:
            sõnastik[i] += 1
    return sõnastik
def grupeeri(sag):
    sõnastik = {}
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Täishäälikud"] = set()
    sõnastik["Muud"] = set()
    sagedused = sümbolite_sagedus(sag)
    
    for i in sagedused:
        if i.lower in "bcdfghjklmnpqrsšzžtvwxy":
            sõnastik["Kaashäälikud"].add((i, sagedused[i]))
        elif i.lower in "aeiouõäöü":
            sõnastik["Täishäälikud"].add((i, sagedused[i]))
        else:
            sõnastik["Muud"].add((i,sagedused[i]))
    return sõnastik
