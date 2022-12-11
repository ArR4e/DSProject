import string

def erinevad_sümbolid(sõne):
    hulk = set()
    for sümbol in sõne:
        hulk.add(sümbol)
    return hulk

def sümbolite_sagedus(sõne1):
    sõnastik1 = {}
    for täht in sõne1:
        if täht in sõnastik1:
            sõnastik1[täht] = sõnastik1[täht] + 1
        else:
            sõnastik1[täht] = 1
    return sõnastik1

def grupeeri(sõne):
    sõnastik1 = sümbolite_sagedus(sõne)
    sõnastik2 = {}
    sõnastik2["Täishäälikud"] = set()
    sõnastik2["Kaashäälikud"] = set()
    sõnastik2["Muud"] = set()
    täishäälikud = ["a", "e", "i", "o", "u", "ü", "õ", "ö", "ä"]
    kaashäälikud = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "š", "z", "ž", "t", "v", "w", "y", "x"] 
    muud = list(string.punctuation) + [" "]
    for täht in sõne:
        väiketäht = täht.lower()
        if väiketäht in täishäälikud:
            sõnastik2["Täishäälikud"].add((täht, sõnastik1[täht]))
                    
        elif väiketäht in kaashäälikud:
            sõnastik2["Kaashäälikud"].add((täht, sõnastik1[täht]))
                    
        elif väiketäht in muud:
            sõnastik2["Muud"].add((täht, sõnastik1[täht]))
                    
    return sõnastik2