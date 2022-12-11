def erinevad_sümbolid(sõne):
    jrj = list(sõne)
    v = set(jrj)
    return v
def sümbolite_sagedus(sõne):
    jrj = list(sõne)
    v = set(jrj)
    vastus = {}
    for el in v:
        kogus = jrj.count(el)
        vastus[el] = kogus
    return vastus
def grupeeri(sõne):
    vastus = {}
    vastus["Täishäälikud"] = set()
    vastus["Kaashäälikud"] = set()
    vastus["Muud"] = set()
    täishäälik = list("iüueöõoäa")
    kaashäälik = list("bcdfghjklmnpqrsšzžtvwxy")
    sõnastik = sümbolite_sagedus(sõne)
    for el in sõnastik:
        if el.lower() in täishäälik:
            vastus["Täishäälikud"].add((el, sõnastik[el]))
        elif el.lower() in kaashäälik:
            vastus["Kaashäälikud"].add((el, sõnastik[el]))
        else:
            vastus["Muud"].add((el, sõnastik[el]))
    return vastus