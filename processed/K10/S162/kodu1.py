def erinevad_sümbolid(sõne):
    sõne=sõne.strip()
    erinevad=set()
    for täht in list(sõne):
        erinevad.add(täht)
    return erinevad

def sümbolite_sagedus(sõne):
    sõne=sõne.strip()
    sagedus={}
    for täht in list(sõne):
        if täht in sagedus:
            sagedus[täht]+=1
        else:
            sagedus[täht]=1
    return sagedus

def grupeeri(sõne):
    grupid={}
    grupid['Täishäälikud']=set()
    grupid['Kaashäälikud']=set()
    grupid['Muud']=set()
    täishäälikud='aeiouõäöüAEIOUÕÄÖÜ'
    kaashäälikud='bcdfghjklmnpqrsšžztvwxyBCDFGHJKLMNPQRSŠŽZTVWXY'
    for el in sümbolite_sagedus(sõne):
        if el in täishäälikud:
            a=(el,(sümbolite_sagedus(sõne)[el]))
            grupid['Täishäälikud'].add(a)
        elif el in kaashäälikud:
            a=(el,(sümbolite_sagedus(sõne)[el]))
            grupid['Kaashäälikud'].add(a)
        else:
            a=(el,(sümbolite_sagedus(sõne)[el]))
            grupid['Muud'].add(a)
    return grupid
print(grupeeri("sõida tasa üle silla??????)()=/)=/jkdfhjks"))