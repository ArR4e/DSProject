def erinevad_sümbolid(sone):
    sümbolid=set(sone)
    return sümbolid

def sümbolite_sagedus(sone):
    sagedus={}
    sümbolid=erinevad_sümbolid(sone)
    for el in sone:
        sagedus[el]=sagedus.get(el,0)+1
    return sagedus

def grupeeri(sone):
    vok="AaEeIiOoUuÕõÄäÖöÜü"
    kons="BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsZzTtVvWwXxYy"
    grupeering={"Täishäälikud":set(),"Kaashäälikud":set(),"Muud":set() }
    sagedus=sümbolite_sagedus(sone)
    for võti,väärtus in sagedus.items():
        if võti in vok:
            grupeering["Täishäälikud"].add((võti, väärtus))
        elif võti in kons:
            grupeering["Kaashäälikud"].add((võti, väärtus))
        else:
            grupeering["Muud"].add((võti, väärtus))
    return grupeering
