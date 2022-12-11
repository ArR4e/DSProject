def erinevad_sümbolid(lause):
    return set(lause)

def sümbolite_sagedus(lause):
    sõnastik = {}
    sümbolid = list(lause)
    for sümbol in sümbolid:
        if sümbol in sõnastik:
            sõnastik[sümbol] = sõnastik[sümbol] + 1
        else:
            sõnastik[sümbol] = 1
    return sõnastik
    
def grupeeri(lause):
    täishäälikud = list("aeiouõäöüAEIOUÕÄÖÜ")
    kaashäälikud = list("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM")
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    for sümbol in lause:
        if sümbol in täishäälikud:
            sõnastik["Täishäälikud"].add((sümbol, lause.count(sümbol)))
        elif sümbol in kaashäälikud:
            sõnastik["Kaashäälikud"].add((sümbol, lause.count(sümbol)))
        else:
            sõnastik["Muud"].add((sümbol, lause.count(sümbol)))
    return(sõnastik)
    
    
#lause = "sõida tasa üle silla"
#erinevad_sümbolid(lause)
#sümbolite_sagedus(lause)
#grupeeri(lause)