def erinevad_sümbolid(n):
    return set(n)
# print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(n):
    hulgad = {}
    for taht in n:
        hulgad[taht] = hulgad[taht] + 1 if taht in hulgad else 1
    return hulgad
# print(sümbolite_sagedus("hulk ei sisalda kunagi korduvaid elemente"))
    
def grupeeri(n):
    thaalik = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    khaalik = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "š", "z", "ž", "t", "v", "c","x","y","w","q"]
    tais_h = {}
    kaas_h = {}
    muud = {}
    for i in n:
        if i in thaalik or i.lower() in thaalik:
            tais_h[i] = tais_h[i]+1 if i in tais_h else 1
        if i in khaalik or i.lower() in khaalik:
            kaas_h[i] = kaas_h[i]+1 if i in kaas_h else 1
        if i not in thaalik and i not in khaalik and i.lower() not in thaalik and i.lower() not in khaalik:
            muud[i] = muud[i]+1 if i in muud else 1
    tais = tais_h.items()
    taisv = set(tais)
    kaas = kaas_h.items()
    kaasv = set(kaas)
    muu = muud.items()
    muus = set(muu)
    koos = {"Täishäälikud":taisv, "Kaashäälikud":kaasv, "Muud":muus}
    return koos
# print(grupeeri("Sõida Tasa üle silla"))
    
        