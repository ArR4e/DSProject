def seosta_lapsed_ja_vanemad(laste_nimi_fail, nimi_fail):
    laste_nimi = open(laste_nimi_fail, "r")
    nimed = open(nimi_fail, "r")
    _id_koodid = laste_nimi.read().splitlines()
    _isik_id_kood = nimed.read().splitlines()
    
    sonastik_vanemad_laps_id = {}
    for line1 in _id_koodid:
        elemendid1 = line1.split()
        for el1 in elemendid1:
            if el1 not in sonastik_vanemad_laps_id:
                sonastik_vanemad_laps_id[elemendid1[0]] = elemendid1[1] 
    sonastik_id_nimi = {}
    
    for line2 in _isik_id_kood:
        elemendid2 = line2.split()
        for el2 in elemendid2:
            if el2 not in sonastik_id_nimi:
                 sonastik_id_nimi[elemendid2[0]] = elemendid2[1] +" "+ elemendid2[2]
    
    sonastik_laps_ja_vanemad_nimi = {}
    
    for i in sonastik_id_nimi:
        for j in sonastik_vanemad_laps_id:
            if i == j:
                 sonastik_laps_ja_vanemad_nimi[sonastik_id_nimi[sonastik_vanemad_laps_id[j]]] = sonastik_id_nimi[i]
                   
    return(sonastik_laps_ja_vanemad_nimi)
    
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))