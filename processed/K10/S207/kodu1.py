def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    nimekiri = {}
    for täht in set(sõne):
        nimekiri[täht] = sõne.count(täht)
    return nimekiri

def grupeeri(sõne):
    täishäälikudnimekiri = set("aeoiuõäöüAEIOUÕÄÖÜ")
    kaashäälikudnimekiri = set("qwrtypsdfghjklzxcvbnmžšQWERTYPSDFGHJKLZXCVBNMŽŠ")
    täishäälikud = set()    
    kaashäälikud = set()
    muud = set()
    nimekiri = {}
    for täht in set(sõne):
        if täht in täishäälikudnimekiri:
            täishäälikud.add((täht, sõne.count(täht)))
        elif täht in kaashäälikudnimekiri:
            kaashäälikud.add((täht, sõne.count(täht)))
        else:
            muud.add((täht, sõne.count(täht)))
    
    nimekiri["Täishäälikud"] = täishäälikud
    nimekiri["Kaashäälikud"] = kaashäälikud
    nimekiri["Muud"] = muud
    return nimekiri