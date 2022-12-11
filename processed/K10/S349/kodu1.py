from collections import defaultdict, Counter
#see on sümbolite_sageduse jaoks

def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        sõnastik[täht] = sõnastik.get(täht, 0) +1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    kõik = (sümbolite_sagedus(sõne))
    for võti in kõik:
        if võti in ["a","A","e","E","i","I","o","O","u","U","õ","Õ","ä","Ä","ö","Ö","ü","Ü"]:
            sõnastik["Täishäälikud"].add((võti, kõik[võti]))
        elif võti in ["b","B","c","C","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","p","P","r","R","s","S","š","Š","z","Z","ž","Ž","t","T","v","V","W","w","x","X","y","Y","q","Q"]:
            sõnastik["Kaashäälikud"].add((võti, kõik[võti]))
        else:
            sõnastik["Muud"].add((võti, kõik[võti]))
    return sõnastik

print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

print(sümbolite_sagedus("Hei hopsti, väikevend!"))

print(grupeeri("sõida tasa üle silla"))






