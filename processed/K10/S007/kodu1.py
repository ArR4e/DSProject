def erinevad_sümbolid(sõne):
    a = set(sõne)
    return a

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        if el in sõnastik:
            sõnastik[el] = sõnastik[el] + 1
        else:
            sõnastik[el] = 1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    täishäälik = "aeiouõäöü"
    täishäälikud = set(täishäälik)
    kaashäälik = "kptgbdfhszjlmnrvšzywcqx"
    kaashäälikud = set(kaashäälik)
    y = sümbolite_sagedus(sõne)
    
    for täht in y:
        if täht.lower() in täishäälikud:
            sõnastik["Täishäälikud"].add((täht,y[täht]))
        elif täht.lower() in kaashäälikud:
            sõnastik["Kaashäälikud"].add((täht, y[täht]))
        else:
            sõnastik["Muud"].add((täht, y[täht]))
 
        
    return sõnastik
        
print(grupeeri("sõida tasa üle silla"))