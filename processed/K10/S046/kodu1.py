def erinevad_sümbolid(sõne):
    tähed = set()
    for täht in sõne:
        tähed.add(täht)
    return tähed
def sümbolite_sagedus(sõne):
    sagedus = {}
    tähed = erinevad_sümbolid(sõne)
    for täht in tähed:
        sagedus[täht] = sõne.count(täht)
    return(sagedus)
def grupeeri(sõne):
    täis = "aeiouöäõüAEIOUÖÄÕÜ"
    kaas = "bdfghjklmnprsšzžtvxczyqwBDFGHJKLMNPRSŠZŽTVXCZYQW"
    sagedus = sümbolite_sagedus(sõne)
    täish = set()
    kaash = set()
    muu = set()
    grupeering = {}
    for täht in sagedus:
        if täht in täis:
            täish.add((täht,sagedus[täht]))
        elif täht in kaas:
            kaash.add((täht,sagedus[täht]))
        else:
            muu.add((täht,sagedus[täht]))
    grupeering["Täishäälikud"] = täish
    grupeering["Kaashäälikud"] = kaash
    grupeering["Muud"] = muu
    return(grupeering)
