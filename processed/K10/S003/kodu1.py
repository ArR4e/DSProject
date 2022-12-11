def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for tähemärk in sõne:
        if tähemärk in sõnastik :
            sõnastik[tähemärk] = sõnastik[tähemärk] + 1
        else :
            sõnastik[tähemärk] = 1
    return sõnastik

def grupeeri(sõne) :
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    sagedus = sümbolite_sagedus(sõne)
    for key in sagedus:
        if key.lower() in "aeiouõäöü" :
            sõnastik["Täishäälikud"].add((key,sagedus[key]))
        elif key.lower() in "qxcwbydfghjklmnprsztvžš" :
            sõnastik["Kaashäälikud"].add((key,sagedus[key]))
        else:
            sõnastik["Muud"].add((key,sagedus[key]))
                
    return sõnastik
            