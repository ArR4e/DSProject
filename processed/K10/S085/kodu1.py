def erinevad_sümbolid(sõne):
    hulk = set()
    for i in sõne:
        hulk.add(i)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        sõnastik[i] = sõne.count(i)
    return sõnastik
    
def grupeeri(sõne):
    sõnastik = {}
    sümbolid = sümbolite_sagedus(sõne)
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] =set()
    sõnastik["Muud"] = set()
    for i in sümbolid:
        if i.lower() in "aeiouüöäõ" :  
            sõnastik["Täishäälikud"].add((i, sümbolid[i]))
        elif i.lower() in "kptgbdlmnvjrshfšzžwqyxc":
            sõnastik["Kaashäälikud"].add((i,sümbolid[i]))
        else:
            sõnastik["Muud"].add((i, sümbolid[i]))
    return sõnastik
