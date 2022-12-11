def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõne_järjend = list(sõne)
    sõnastik = {}
    for täht in sõne_järjend:
        sõnastik[täht] = sõnastik.get(täht,0) + 1
    return sõnastik

täishäälikud = "aeiouõäöü"
kaashäälikud = "bcdfghjklmnprsšzžtvxwyq"
def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    sõnastik1 = sümbolite_sagedus(sõne)
    for võti,väärtus in sõnastik1.items():
        if võti.lower() in täishäälikud:
            sõnastik["Täishäälikud"].add((võti,väärtus))
        elif võti.lower() in kaashäälikud:
            sõnastik["Kaashäälikud"].add((võti,väärtus))
        else:
            sõnastik["Muud"].add((võti,väärtus))
    return sõnastik
    