def erinevad_sümbolid(sone):
    hulk = set()
    for taht in sone:
        hulk.add(taht)
    return hulk

def sümbolite_sagedus(sone):
    sonastik = {}
    for taht in sone:
        sonastik[taht] = sone.count(taht)
    return sonastik
    
def grupeeri(sone):
    sonastik = {}
    taishaalikud = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü", "A", "E", "I", "O", "U", "Õ", "Ä", "Ö", "Ü"]
    kaashaalikud = ["l", "m", "n", "r", "s", "h", "v", "j", "k", "p", "t", "g", "b", "d", "c", "f", "q", "z", "w", "x", "y", "L", "M", "N", "R", "S", "H", "V", "J", "K", "P", "T", "G", "B", "D", "C", "F", "Q", "Z", "W", "X", "Y"]
    taishaalikute_hulk = set()
    kaashaalikute_hulk = set()
    muud_hulk = set()
    for taht in sone:
        if taht in taishaalikud:
            taishaalikute_hulk.add((taht, sone.count(taht)))
        elif taht in kaashaalikud:
            kaashaalikute_hulk.add((taht, sone.count(taht)))
        else:
            muud_hulk.add((taht, sone.count(taht)))
    sonastik["Täishäälikud"] = taishaalikute_hulk
    sonastik["Kaashäälikud"] = kaashaalikute_hulk
    sonastik["Muud"] = muud_hulk
    return sonastik