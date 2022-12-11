def erinevad_sümbolid(sõne):
    sümbolid = set()
    for täht in sõne:
        if täht in sümbolid:
            continue
        else:
            sümbolid.add(täht)
    return sümbolid

def sümbolite_sagedus(sõne):
    sümbolid = {}
    for täht in sõne:        
        if täht in sümbolid:
            tähearv = sümbolid.get(täht) + 1
        else:
            tähearv = 1
        sümbolid[täht] = tähearv
    return sümbolid

def grupeeri(sõne):
    täishäälikud = 'AEIOUÕÄÖÜaeiouõäöü'
    kaashäälikud = 'VJLMNRSHFŠZŽKGPBTDWXYQCvjlmnrshfšzžkgpbtdwxyqc'
    täislist = []
    kaaslist = []
    muudlist = []
    täisdict = {}
    kaasdict = {}
    muuddict = {}
    täisset = set()
    kaasset = set()
    muudset = set()
    grupeeritud = {}
    for täht in sõne:
        if täht in täishäälikud:
            täislist.append(täht)
        elif täht in kaashäälikud:
            kaaslist.append(täht)
        else:
            muudlist.append(täht)
    for täht in täislist:
        if täht in täisdict:
            tähearv = täisdict.get(täht) + 1
        else:
            tähearv = 1
        täisdict[täht] = tähearv
    for key in täisdict:
        tähearv = täisdict.get(key)
        ennik = (key, tähearv)
        täisset.add(ennik)
    for täht in kaaslist:
        if täht in kaasdict:
            tähearv = kaasdict.get(täht) + 1
        else:
            tähearv = 1
        kaasdict[täht] = tähearv
    for key in kaasdict:
        tähearv = kaasdict.get(key)
        ennik = (key, tähearv)
        kaasset.add(ennik)
    for täht in muudlist:
        if täht in muuddict:
            tähearv = muuddict.get(täht) + 1
        else:
            tähearv = 1
        muuddict[täht] = tähearv
    for key in muuddict:
        tähearv = muuddict.get(key)
        ennik = (key, tähearv)
        muudset.add(ennik)
    grupeeritud["Täishäälikud"] = täisset
    grupeeritud["Kaashäälikud"] = kaasset
    grupeeritud["Muud"] = muudset
    return grupeeritud
