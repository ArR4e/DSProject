vanem_laps = open("lapsed.txt", "r", encoding = "UTF - 8")
id_nimi = open("nimed.txt", "r", encoding = "UTF - 8")
    
def seosta_lapsed_ja_vanemad(vanem_laps, id_nimi):
    seos = {}
    vanemad = {}
    lõplik = {}
    for rida in vanem_laps:
        vanema_id, lapse_id = rida.strip().split(" ", 1)
        if lapse_id in seos:
            seos[lapse_id] = ((seos[lapse_id]) + ", " + vanema_id)
        else:
            seos[lapse_id] = vanema_id
    for line in id_nimi:
        idkood, nimi = line.strip().split(" ", 1)
        for key in seos:
            if key == idkood:
                lõplik[nimi] = seos[key]
    
    return lõplik
