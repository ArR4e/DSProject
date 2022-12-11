def erinevad_sümbolid(sõne):
    erinevad = set(sõne)
    return erinevad

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for tm in sõne: #tm = tähemärk
        sõnastik[tm] = sõnastik.get(tm, 0) + 1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    sümbolid = erinevad_sümbolid(sõne)
    kordused = sümbolite_sagedus(sõne)
    for täht in kordused:
        if täht.lower() in "aeiouõäöü":
            sõnastik["Täishäälikud"].add((täht,int(kordused[täht])))
        elif täht.lower() in "bdfghjklmnprsšzžtvywqxc":
            sõnastik["Kaashäälikud"].add((täht,int(kordused[täht])))
        else:
            sõnastik["Muud"].add((täht,int(kordused[täht])))
    return(sõnastik)
        
grupeeri("Heihopsti, väikevend!")