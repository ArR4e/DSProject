def erinevad_sümbolid(sõne):
    erinevate_sümbolite_hulk = set(sõne)
    return erinevate_sümbolite_hulk

def sümbolite_sagedus(sõne):
    sagedus = {}
    for täht in sõne:
        sagedus[täht] = sagedus.get(täht, 0)+1   
    return sagedus

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    täishäälikud = "AEIOUÄÖÜÕaeiouäöüõ"
    kaashäälikud = "BCDFGHJKLMNPRQSZTVXWYbcdfghjklmnpqrsztvxwy"
    sagedus2 = sümbolite_sagedus(sõne)
    for häälik in sagedus2:
        if häälik in täishäälikud:
            täishäälikute_ennik = (häälik,sagedus2.get(häälik))
            sõnastik["Täishäälikud"].add(täishäälikute_ennik)
        elif häälik in kaashäälikud:
            kaashäälikute_ennik  = (häälik,sagedus2.get(häälik))
            sõnastik["Kaashäälikud"].add(kaashäälikute_ennik)
        else:
            muud_ennik = (häälik, sagedus2.get(häälik))
            sõnastik["Muud"].add(muud_ennik)
            
    return sõnastik
    
#sõne = "hulk ei sisalda kunagi korduvaid elemente"
#sõne = "Hei hopsti, väikevend!"
#sõne = "sõida tasa üle silla"
#print(erinevad_sümbolid(sõne))
#print(sümbolite_sagedus(sõne))
#print(grupeeri(sõne))
