def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
        if sümbol not in sõnastik:
            sõnastik[sümbol] = 1
        elif sümbol in sõnastik:
            sõnastik[sümbol] = sõnastik[sümbol]+1
    return sõnastik
def grupeeri(sõne):
    sõnastik = {}
    täishäälikud1 = {"a","e","i","o","u","õ","ä","ö","ü"}
    kaashäälikud1 = {"b","c","d","f","g","h","j","k","l","m","n","p","g","r","s","š","z","t","v","w","x","y","q"}
    elemendid = sümbolite_sagedus(sõne)
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    for sümbol in elemendid:
        if sümbol.lower() in täishäälikud1:
            sõnastik["Täishäälikud"].add((sümbol,elemendid[sümbol]))
        elif sümbol.lower() in kaashäälikud1:
            sõnastik["Kaashäälikud"].add((sümbol,elemendid[sümbol]))
        else:
            sõnastik["Muud"].add((sümbol,elemendid[sümbol]))
    return sõnastik