def erinevad_sümbolid(a):
    h = set(a)
    return h

def sümbolite_sagedus(a):
    h = {}
    for el in a:
        h[el] = h.get(el, 0) + 1
    return h

def grupeeri(a):
    h = {"Täishäälikud" : {},
         "Kaashäälikud" : {},
         "Muud" : {}}
    h1 = {}
    h2 = {}
    h3 = {}
    
    täish = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Õ", "õ", "Ä", "ä", "Ö", "ö", "Ü", "ü"]
    kaash = ["B", "b", "C", "c", "D", "d", "F", "f", "G", "g", "H", "h", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "P", "p", "Q", "q", "R", "r", "S", "s", "Š", "š", "Z", "z", "Ž", "ž", "T", "t", "V", "v", "W", "w", "X", "x", "Y", "y"]
    
    # sõnastik
    for el in a:
        if el in täish:
            h1[el] = (h1.get(el, 0) + 1)
        elif el in kaash:
            h2[el] = h2.get(el, 0) + 1
        else:
            h3[el] = h3.get(el, 0) + 1
    
    # hulgad
    h4 = set()
    h5 = set()
    h6 = set()
    
    for el in h1:
        h4.add((el, h1.get(el)),)
    for el in h2:
        h5.add((el, h2.get(el)),)
    for el in h3:
        h6.add((el, h3.get(el)),)
    
    # hulgad sõnastiku sisse
    h["Täishäälikud"] = h4
    h["Kaashäälikud"] = h5
    h["Muud"] = h6
    
    return h