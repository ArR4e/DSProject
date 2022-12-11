def erinevad_sümbolid(sõne):
    hulk=set()
    sümbolid=list(sõne)
    for täht in sümbolid:
        hulk.add(täht)
    return hulk

def sümbolite_sagedus(sõne):
    sümbolid={}
    tähed=list(sõne)
    for täht in tähed:
        if täht in sümbolid:
            x=sümbolid[täht]+1
            sümbolid[täht]=x
        else:
            sümbolid[täht]=1
    return sümbolid


def grupeeri(sõne):
    häälikud={}
    täis=set()
    häälikud['Täishäälikud']=täis
    kaas=set()
    häälikud['Kaashäälikud']=kaas
    muu=set()
    häälikud['Muud']=muu
    tähed=list(sõne)
    for täht in tähed:
        mitu=tähed.count(täht)
        täishäälikud=['a','e','i','o','u','õ','ä','ö','ü']
        if täht.lower() in täishäälikud:
            paar=(täht,mitu)
            täis.add(paar)
            häälikud['Täishäälikud']=täis          
        elif täht.isalpha():
            paar=(täht,mitu)
            kaas.add(paar)
            häälikud['Kaashäälikud']=kaas
        else:
            paar=(täht,mitu)
            muu.add(paar)
            häälikud['Muud']=muu
    return häälikud
