def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk
def sümbolite_sagedus(sõne):
    sõnastik = {}
    sõnastik = {i:sõne.count(i) for i in erinevad_sümbolid(sõne)}
    return sõnastik
def grupeeri(sõne):
    sümbolite_segu = sümbolite_sagedus(sõne)
    grupp = {}
    täishäälikud = set()
    kaashäälikud = set()
    muud = set()
    for t, k in sümbolite_segu.items():
        if t in "AaEeIiOoUuÕõÄäÖöÜü":
            täishäälikud.add((t, k))
        elif t in "BbCcDdFfGgHhJjKkLlMmNnPpRrQqSsŠšZzŽžTtVvWwXxYy":
            kaashäälikud.add((t, k))
        else:
            muud.add((t, k))
    grupp["Täishäälikud"] = täishäälikud
    grupp["Kaashäälikud"] = kaashäälikud
    grupp["Muud"] = muud
    return grupp