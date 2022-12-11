def erinevad_sümbolid(sõne):
    hulk=set()
    for täht in sõne:
        hulk.add(täht)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        if täht in sõnastik:
            sõnastik[täht]+= 1
        else:
            sõnastik[täht]= 1
    return sõnastik

def grupeeri(sõne):
    Täishäälik = ("aeiouõüöäAEIOUÕÜÖÄ")
    Kaashäälik = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    Täishäälikud= set()
    Kaashäälikud=set()
    Muud= set()
    tähed = {}
    sageduse_sõnastik = sümbolite_sagedus(sõne) #võti on sümbol ja võtmele vastv väärtus sümboli eisnemiste arv sõnes
    # {"a" : 0}
    
    for el in sõne:
        if el in Täishäälik:
            Täishäälikud.add((el, sageduse_sõnastik[el]))
        elif el in Kaashäälik:
            Kaashäälikud.add((el, sageduse_sõnastik[el]))
        else:
            Muud.add((el, sageduse_sõnastik[el]))
            
            
    tähed["Täishäälikud"] = Täishäälikud
    tähed["Kaashäälikud"] = Kaashäälikud
    tähed["Muud"] = Muud
    return tähed
    