def erinevad_sümbolid(tekst):
    return set(tekst)
def sümbolite_sagedus(tekst):
    sümbolid = {}
    for el in erinevad_sümbolid(tekst):
        sümbolid[el] = tekst.count(el)
    return sümbolid
def grupeeri(tekst):
    täishäälikud = set("aeiouõäöüAEIOUÕÄÖÜ")
    kaashäälikud = set("bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTVWXY")
    sümboleid = erinevad_sümbolid(tekst)
    täishäälikuid = sümboleid & täishäälikud
    kaashäälikuid = sümboleid & kaashäälikud
    muid = sümboleid - täishäälikud - kaashäälikud
    grupp = {}
    täishset = set()
    kaashset = set()
    muuset = set()
    for el in täishäälikuid:
        täishset.add((el,tekst.count(el)))
    for el in kaashäälikuid:
        kaashset.add((el,tekst.count(el)))
    for el in muid:
        muuset.add((el,tekst.count(el)))
    grupp["Täishäälikud"] = täishset
    grupp["Kaashäälikud"] = kaashset
    grupp["Muud"] = muuset
    return grupp