from collections import Counter
def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    a=Counter(sõne)
    a=dict(a)
    return a
def grupeeri(sõne):
    grupeeritud={"Täishäälikud" : set(), "Kaashäälikud" : set(), "Muud" : set()}
    täishäälikud={"a", "e", "i", "o", "u", "ö", "ä", "ü", "õ"}
    kaashäälikud={"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r",
                "s", "š", "z", "ž", "t", "v", "w", "x", "y"}
    a=dict(Counter(sõne))
    sagedused=[(m,n) for m, n in a.items()]
    for i in sagedused:
        if i[0].lower() in täishäälikud:
            grupeeritud["Täishäälikud"].add(i)
        elif i[0].lower() in kaashäälikud:
            grupeeritud["Kaashäälikud"].add(i)
        else:
            grupeeritud["Muud"].add(i)
    return grupeeritud        
    
