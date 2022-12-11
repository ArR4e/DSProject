def erinevad_sümbolid(sõne):
    hulk = set()
    for täht in sõne:
        hulk.add(täht)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        if täht in sõnastik:
            sõnastik[täht] = sõnastik[täht]+1
        if täht not in sõnastik:
            sõnastik[täht] = 1
    return sõnastik 
    
def grupeeri(sõne):
    sõnastik = {}
    Täishäälikud = "aeiouõäöü"
    Kaashäälikud = "bcdfghjklmnpqrsšzžtvwxy"
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()     
    teinesõnastik = sümbolite_sagedus(sõne)
    for võti in teinesõnastik:
        võti2 = võti.lower()
        if võti2 in Täishäälikud:
            sõnastik["Täishäälikud"].add((võti, teinesõnastik.get(võti)))
        if võti2 in Kaashäälikud:
            sõnastik["Kaashäälikud"].add((võti, teinesõnastik.get(võti)))
        if võti2 not in Täishäälikud:
            if võti2 not in Kaashäälikud:
                sõnastik["Muud"].add((võti, teinesõnastik.get(võti)))
    return sõnastik

print(grupeeri("Toas on lärmakas!"))
    
    