def seosta_lapsed_ja_vanemad (lapsed, nimed):
    nimefail = open(nimed)
    lastefail = open(lapsed)
    sõnastik = {}
    laste_sõnastik = {}
    for rida in nimefail:
        isikukood, eesnimi, perenimi = rida.split(" ")
        täisnimi = eesnimi + " " + perenimi.strip()
        sõnastik[isikukood] = täisnimi
    for rida in lastefail:
        vanema_ik, lapse_ik = rida.strip().split(" ")
        lapse_nimi = sõnastik[lapse_ik]
        vanema_nimi = sõnastik[vanema_ik]
        if lapse_nimi in laste_sõnastik:
            laste_sõnastik[lapse_nimi] = {("".join(laste_sõnastik[lapse_nimi])), vanema_nimi}
        else:
            laste_sõnastik[lapse_nimi] = {vanema_nimi}
    return laste_sõnastik
    nimefail.close()
    lastefail.close()