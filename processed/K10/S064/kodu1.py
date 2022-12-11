# 1. Teksti analüüs

sõne = "Tere hommikust!"

def erinevad_sümbolid(sõne):
    sümbolid = set(sõne)
    return(sümbolid)

def sümbolite_sagedus(sõne):
    sõnastik = list(sõne)
    uus = {}
    for sümbol in sõnastik:
        uus[sümbol] = sõnastik.count(sümbol)
    return(uus)

def grupeeri(sõne):
    uus = {}
    esimene = set()
    teine = set()
    kolmas = set()
    täishäälikud = "aeiouüõöäAEIOUÜÕÖÄ"
    kaashäälikud = "kptgbdqwrysfhjklzxcvnmQWRTYPSDFGHJKLZXCVBNM"
    muud = ",.-_:;!?' "
    sõnastik = list(sõne)
    for sümbol in sõnastik:
        uus["Täishäälikud"] = esimene
        uus["Kaashäälikud"] = teine
        uus["Muud"] = kolmas
        if sümbol in täishäälikud:
            uus["Täishäälikud"].add((sümbol, sõnastik.count(sümbol)))
        elif sümbol in kaashäälikud:
            uus["Kaashäälikud"].add((sümbol, sõnastik.count(sümbol)))
        elif sümbol in muud:
            uus["Muud"].add((sümbol, sõnastik.count(sümbol)))
    return(uus)

print(erinevad_sümbolid(sõne))
print(sümbolite_sagedus(sõne))
print(grupeeri(sõne))