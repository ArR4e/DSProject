# erinevad_sümbolid('hulk ei sisalda kunagi korduvaid elemente')
# sümbolite_segadus('hulk ei sisalda kunagi korduvaid elemente')
# grupeeri('hulk ei sisalda kunagi korduvaid elemente')

def erinevad_sümbolid(sõne):
    return set(sõne)

print(erinevad_sümbolid('hulk ei sisalda kunagi korduvaid elemente'))

sõnastik = {}

def sümbolite_segadus(lause):
    for el in lause:
        if el in sõnastik:
            sõnastik[el] += 1
        else:
            sõnastik[el] = 1
    return sõnastik

print(sümbolite_segadus('hulk ei sisalda kunagi korduvaid elemente'))
        

def grupeeri(tekst):
    täish = ("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
    kaash = ("b", "d", "f", "g", "h", "j",
          "k", "l", "m", "n", "p", "r",
          "š", "s", "ž", "z", "t", "v")
    täish_dict = {}
    kaash_dict = {}
    muud = {}
    
    täish_set = set()
    kaash_set = set()
    muud_set = set()
    
    for ch in tekst:
        if ch in täish:
            if ch in täish_dict:
                täish_dict[ch] += 1
            else:
                täish_dict[ch] = 1
                
        elif ch in kaash:
            if ch in kaash_dict:
                kaash_dict[ch] += 1
            else:
                kaash_dict[ch] = 1
        else:
            if ch in muud:
                muud[ch] += 1
            else:
                muud[ch] = 1
    
    for key in täish_dict:
        value = täish_dict[key]
        täish_set.add((key, value))
    for key in kaash_dict:
        value = kaash_dict[key]
        kaash_set.add((key, value))
    for key in muud:
        value = muud[key]
        muud_set.add((key, value))
    return {"Täishäälikud": täish_set,
            "Kaashäälikud": kaash_set,
            "Muud": muud_set}
        
        
print(grupeeri('hulk ei sisalda kunagi korduvaid elemente'))

            
    
    
