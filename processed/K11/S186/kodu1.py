def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    sõnastik={}
    vanemad=[]
    lapsed=[]
    vanem_laps_kood=open(lastefailinimi)
    kood_nimi=open(nimedefailinimi)
    for rida in vanem_laps_kood:
        rida.split(" ")
        vanemad.append(rida[0])
        lapsed.append(rida[1])
    for rida in kood_nimi:
        rida.split(" ", 1)
        sõnastik[rida[0]]=rida[1]
    lõppsõnastik={}
    for key in sõnastik:
        lõppsõnastik[sõnastik[key]]=vanemad(lapsed.index(key))