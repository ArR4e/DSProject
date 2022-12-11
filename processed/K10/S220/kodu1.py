def erinevad_sümbolid(sõne):
    sümbolid = []
    for el in sõne:
        if el not in sümbolid :
            sümbolid.append(el)
    return sümbolid
            
#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
    
    
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne :
        mitu = sõne.count(el)
        sõnastik[el] = mitu
    return sõnastik

#print(sümbolite_sagedus("Hei"))

def grupeeri(sõne):
    sõne = sõne.lower()
    sõnastik = {"täishäälikud" : "" , "kaashäälikud" : "", "muud_sümbolid": ""}
    täishäälikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaashäälikud = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "z", "t", "v"]
    elemendid = sümbolite_sagedus(sõne)
    täish = []
    kaash = []
    muud = []
    for el in elemendid :
        if el in täishäälikud :
            a =(el, elemendid[el])
            täish.append(a)
        elif el in kaashäälikud :
            b = (el, elemendid[el])
            kaash.append(b)
        else :
            c = (el, elemendid[el])
            muud.append(c)
    sõnastik["täishäälikud"] = täish
    sõnastik["kaashäälikud"] = kaash
    sõnastik["muud_sümbolid"] = muud
    return sõnastik 
    
print(grupeeri("Hei"))
    
        
    