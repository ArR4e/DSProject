def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    sagedus={}
    for el in sõne:
        if el in sagedus:
            sagedus[el]+=1
        else:
            sagedus[el]=1
    return sagedus
def grupeeri(sõne):
    täishäälikud=set()
    kaashäälikud=set()
    muud=set()
    for täht in 'aeiouõüäöAEIOUÕÜÄÖ':
        if täht in sõne:
            täishäälikud.add((täht,sõne.count(täht)))
    for täht in 'klmnbvcxzsdfghpytrwqjMNBVCXZLKJHGFDSPYTRWQ':
        if täht in sõne:
            kaashäälikud.add((täht,sõne.count(täht)))
    for täht in ' .,!?"-':
        if täht in sõne:
            muud.add((täht,sõne.count(täht)))
    if "'" in sõne:
        muud.add(("'",sõne.count("'")))
    grupid={'Täishäälikud':täishäälikud,'Kaashäälikud':kaashäälikud,'Muud':muud}
    return grupid
print(grupeeri("''Kuule, August! Käes on august?' küsis August ühest august. 'Lõppend august!' vastas August teisest august.'"))