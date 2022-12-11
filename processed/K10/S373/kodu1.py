def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik1 = {}
    for i in sõne:
        if i in sõnastik1:
            sõnastik1[i] += 1
        else:
            sõnastik1[i] = 1
    return sõnastik1

def grupeeri(sõne):
    sõnastik2 = {}
    sõnastik2["Täishäälikud"] = set()
    sõnastik2["Kaashäälikud"] = set()
    sõnastik2["Muud"] = set()
    
    for täht in sõne:
        if täht.lower() in "aeiouõäöü":
            sõnastik2["Täishäälikud"].add((täht, sümbolite_sagedus(sõne).get(täht)))
        elif täht.lower() in "bcdfghjklmnpqrsšzžtvwxy":
            sõnastik2["Kaashäälikud"].add((täht, sümbolite_sagedus(sõne).get(täht)))
        else:
            sõnastik2["Muud"].add((täht, sümbolite_sagedus(sõne).get(täht)))
    return sõnastik2
            