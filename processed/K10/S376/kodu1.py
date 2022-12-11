def erinevad_sümbolid(x):
    hulk = set()
    for el in x:
        if el not in hulk:
            hulk.add(el)
        else:
            continue
    
    return hulk

def sümbolite_sagedus(x):
    sõnastik = {}
    
    for el in x:
        if el in sõnastik:
            sõnastik[el] = sõnastik[el] + 1
        else:
            sõnastik[el] = 1
            
    return sõnastik

def grupeeri(x):
    sõnastik = {}
    täishäälikud = "aeiouõäöü"
    kaashäälikud = "bcdfghjklmnpqrstvwxyz"

    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()

    grupeeritav = sümbolite_sagedus(x)

    for sümbol in grupeeritav:
        if sümbol in täishäälikud or sümbol.lower() in täishäälikud:
            ennik = (sümbol, grupeeritav[sümbol])
            sõnastik["Täishäälikud"].add(ennik)
        elif sümbol in kaashäälikud or sümbol.lower() in kaashäälikud:
            ennik = (sümbol, grupeeritav[sümbol])
            sõnastik["Kaashäälikud"].add(ennik)
        else:
            ennik = (sümbol, grupeeritav[sümbol])
            sõnastik["Muud"].add(ennik)
    
    return sõnastik
