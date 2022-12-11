täishäälikud = ["I", "i", "Ü", "ü", "U", "u", "E", "e", "Ö", "ö", "Õ", "õ", "O", "o", "Ä", "ä", "A", "a"]
kaashäälikud = ["B", "b", "C", "c", "D", "d", "F", "f", "G", "g", "H", "h", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "P", "p", "Q", "q", "R", "r", "S", "s", "Š", "š", "Z", "z", "Ž", "ž", "T", "t", "V", "v", "W", "w", "X", "x", "Y", "y"]

def erinevad_sümbolid(sõne):
    a = set(sõne)
    return a

def sümbolite_sagedus(sõne):
    b = {}
    for taht in erinevad_sümbolid(sõne):
        b[taht] = sõne.count(taht)
    return b
    
def grupeeri(sõne):
    c = {}
    täis = set()
    kaas = set()
    muu = set()
    for taht in sõne:
        if taht in täishäälikud:
            täis.add((taht, sõne.count(taht)))
        elif taht in kaashäälikud:
            kaas.add((taht, sõne.count(taht)))
        else:
            muu.add((taht, sõne.count(taht)))
    c["Täishäälikud"] = täis
    c["Kaashäälikud"] = kaas
    c["Muud"] = muu
    return c
    
    
    
    
    
  
print(grupeeri("hulk ei sisalda kunagi korduvaid elemente"))    
    
    
    
