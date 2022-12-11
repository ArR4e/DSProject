# tagastab kõik sümbolid ühekordselt
def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk



# sõnes sisalduvad tähed: nende esinemissagedus
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
#        if sümbol in sõnastik:
#            sõnastik[sümbol] = sõnastik[sümbol] + 1
#        else:
#            sõnastik[sümbol] = 1
        sõnastik[sümbol] = sõnastik.get(sümbol,0) + 1
        
    return sõnastik





# sõnastik(täishäälikud,kaashäälikud,muud sümbolid)
def grupeeri(sõne):
    sagedus = sümbolite_sagedus(sõne)
    aaa = 'AaEeIiOoUuÕõÄäÖöÜü'
    kaas = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy'
    täishäälikud = {}
    kaashäälikud = {}
    muu = {}
    sõnastik = {}
    for key in sagedus:
        if key in aaa:
            ennik = tuple([(key,sagedus.get(key))])
            täishäälikud.update(ennik)
        elif key in kaas:
            ennik = tuple([(key,sagedus.get(key))])
            kaashäälikud.update(ennik)
        else:
            ennik = tuple(([(key,sagedus.get(key))]))
            muu.update(ennik)
    sõnastik['Täishäälikud'] = täishäälikud
    sõnastik['Kaashäälikud'] = kaashäälikud
    sõnastik['Muud'] = muu

    return sõnastik


print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))
print(sümbolite_sagedus("Hei hopsti, väikevend!"))
print(grupeeri("asõida, tasa, üle, silla"))