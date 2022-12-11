
def erinevad_sümbolid(sõne):
    tähed = list(sõne)
    hulk = set(tähed)
    
    return hulk
    
#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    hulk = erinevad_sümbolid(sõne)
    sõnastik = {}
    for täht in hulk:
        arv = sõne.count(täht)
        sõnastik[täht] = arv
    return sõnastik

#print(sümbolite_sagedus("hulk ei sisalda kunagi korduvaid elementdef e"))

def grupeeri(sõne):
    täishäälikud = "a e i o u õ ä ö ü"
    kaashäälikud = "b c d f g h j k l m n p q r s š z ž t v w x y"
    t=täishäälikud.split()
    k=kaashäälikud.split()
    
    sõnastik = sümbolite_sagedus(sõne)
    
    sõnastik_uus = {}
    t_järjend = []
    k_järjend = []
    muud = []
    for i in sõnastik:
        if i in t:
            t_järjend += [(i, sõnastik[i])]
        elif i in k:
            k_järjend += [(i,sõnastik[i])]
        else:
            muud += [(i,sõnastik[i])]
    
    t_hulk = set(t_järjend)
    k_hulk = set(k_järjend)
    muu_hulk = set(muud)
    
    sõnastik_uus["Täishäälikud"] = t_hulk
    sõnastik_uus["Kaashäälikud"] = k_hulk
    sõnastik_uus["Muud"] = muu_hulk
    return sõnastik_uus
    
grupeeri("odashdf4%¤&%%/&/(37yridsj sf")
    
    
    
    
    
    
    
    
    
    