def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    järjend = list(sõne)
    sõnastik = {}
    for sümbol in järjend:
        sümbolite_arv = järjend.count(sümbol)
        sõnastik[sümbol] = sümbolite_arv
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    järjend = list(sõne)
    täishäälikudhulgana = set()
    kaashäälikudhulgana = set()
    muudhulgana = set()
    täishäälikud = {"a", "e", "i", "o", "u", "õ", "ä", "ö", "ü", "A", "E", "I", "O", "U", "Õ", "Ä", "Ö", "Ü"}
    kaashäälikud = {"q", "Y", "y", "X", "x", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "š", "z", "ž", "t", "v", "w", "B", "D", "F", "Q", "C", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "Š", "Z", "Ž", "T", "V", "W"}
    for sümbol in järjend:
        sümbolite_arv = järjend.count(sümbol)
        if sümbol in täishäälikud:
            ennik = (sümbol, sümbolite_arv)
            täishäälikudhulgana.add(ennik)        
        elif sümbol in kaashäälikud:
            ennik = (sümbol, sümbolite_arv)
            kaashäälikudhulgana.add(ennik)
        else:
            ennik = (sümbol, sümbolite_arv)
            muudhulgana.add(ennik)
    sõnastik["Täishäälikud"] = täishäälikudhulgana
    sõnastik["Kaashäälikud"] = kaashäälikudhulgana
    sõnastik["Muud"] = muudhulgana
    return sõnastik