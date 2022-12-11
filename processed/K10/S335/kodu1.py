def erinevad_sümbolid(sõne):
    sümbolid = set(sõne)
    return sümbolid

def sümbolite_sagedus(sõne):
    tähesõnastik = {}
    järjend = list(sõne)
    for täht in järjend:
        tähesõnastik[täht] = järjend.count(täht)
    return tähesõnastik

def grupeeri(sõne):
    grupp = {"Täishäälikud": None, "Kaashäälikud": None, "Muud": None}
    kaasH_hulk = set()
    täisH_hulk = set()
    muu_hulk = set()
    
    täisH = set("aAeEiIoOuUöÖäÄõÕüÜ")
    kaasH = set("bBcCdDfFgGhHjJkKlLmMnNpPqQrRsSšŠzZžŽtTvVwWxXyY")
    
    sagedused = sümbolite_sagedus(sõne)
    
    for täht in sagedused:
        if täht in täisH:
            täisH_hulk.add((täht, sagedused[täht]))
        elif täht in kaasH:
            kaasH_hulk.add((täht, sagedused[täht]))
        else:
            muu_hulk.add((täht, sagedused[täht]))
    grupp["Täishäälikud"] = täisH_hulk
    grupp["Kaashäälikud"] = kaasH_hulk
    grupp["Muud"] = muu_hulk
    return grupp
print(grupeeri("sõida tasa üle silla"))