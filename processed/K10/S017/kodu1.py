def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        if el not in sõnastik:
            kogus = int(sõne.count(el))
            sõnastik[el] = kogus
    return sõnastik

def grupeeri(sõne):
    vokaalid = "eEUuIioOüÜõÕaAöÖäÄ"
    konsonandid = "qQwWrRtTyYpPsSšŠdDfFgGhHjJkKlLzZžŽxXcCvVbBnNmM"
    täishäälikud = set()
    kaashäälikud = set()
    muud = set()
    sõnastik = {}
    for el in sõne:
        if el in vokaalid:
            if el not in täishäälikud:
                kogus = int(sõne.count(el))
                täishäälikud.add((el, kogus))
        elif el in konsonandid:
            if el not in kaashäälikud:
                kogus = int(sõne.count(el))
                kaashäälikud.add((el, kogus))
        elif el not in muud:
            kogus = int(sõne.count(el))
            muud.add((el, kogus))
    sõnastik["Täishäälikud"] = täishäälikud
    sõnastik["Kaashäälikud"] = kaashäälikud
    sõnastik["Muud"] = muud
    return sõnastik
