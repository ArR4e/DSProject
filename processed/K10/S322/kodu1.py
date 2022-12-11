
def erinevad_sümbolid(sone):
    return set(sone)

def sümbolite_sagedus(sone):
    sagedused = {}
    for täht in erinevad_sümbolid(sone):
        sagedused[täht] = sone.count(täht)
    return sagedused

def grupeeri(sone):
    täishäälikud = erinevad_sümbolid("AEIOUÕÄÖÜYaeiouõäöüy")
    kaashäälikud = erinevad_sümbolid("BCDFGHJKLMNPQRSŠZŽTVXbcdfghjklmnpqrsšzžtvx")
    esin_täishäälikud = erinevad_sümbolid(sone) & täishäälikud
    esin_kaashäälikud = erinevad_sümbolid(sone) & kaashäälikud
    muud_sümbolid = erinevad_sümbolid(sone) ^ (esin_täishäälikud | esin_kaashäälikud)
    # loo paarid
    paarid_täishäälikud = []
    paarid_kaashäälikud = []
    paarid_muud = []
    for täht in esin_täishäälikud: paarid_täishäälikud += [(täht, sone.count(täht))]
    for täht in esin_kaashäälikud: paarid_kaashäälikud += [(täht, sone.count(täht))]
    for täht in muud_sümbolid: paarid_muud += [(täht, sone.count(täht))]
    # tagasta
    return {"Täishäälikud": set(paarid_täishäälikud), "Kaashäälikud": set(paarid_kaashäälikud), "Muud": set(paarid_muud)}

