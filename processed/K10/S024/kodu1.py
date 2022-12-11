def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    d = {}
    järjend = list(sõne)
    for el in järjend:
        if el in d:
            d[el] = d[el] + 1
        else:
            d[el] = 1
#         d[el] = d.get(el, 0) + 1 (võiks ka lühemalt nii eelmise 4 rea asemel)
    return d
    
def grupeeri(sõne):
    d = {}
    täishäälikud = ("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
    kaashäälikud = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "š", "z", "ž", "t", "v", "w", "x", "y")
    järjend = list(sõne)

    täis = set()
    kaas = set()
    muud = set()

    for el in järjend:
        d[el] = d.get(el, 0) + 1
    uus_järjend = [(k, v) for k, v in d.items()]
    
    for i in range(len(uus_järjend)):
        for j in uus_järjend[i][0]:
            if j.lower() in täishäälikud:
               täis.add(uus_järjend[i])
            elif j.lower() in kaashäälikud:
                kaas.add(uus_järjend[i])
            else:
                muud.add(uus_järjend[i])
    
    sõnastik = {}
    sõnastik["Täishäälikud"] = täis
    sõnastik["Kaashäälikud"] = kaas
    sõnastik["Muud"] = muud

    return sõnastik
                
        
        
 