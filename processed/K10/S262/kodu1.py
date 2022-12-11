def erinevad_sümbolid(tekst):
    tagasta = set()
    for el in tekst:
        if el not in tagasta:
            tagasta.add(el)
    return tagasta
def sümbolite_sagedus(tekst):
    tagasta = {}
    for el in tekst:
        if el not in tagasta:
            tagasta[el] = 1
        else:
            tagasta[el] += 1
    return tagasta
def grupeeri(tekst):
    tagasta = {}
    täis = ['a','e','i','o','u','õ','ä','ö','ü','A']
    täish = {}
    täishäälikud = set()
    kaas = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','š','z','ž','t','v','w','x','y','K','L']
    kaash = {}
    kaashäälikud = set()
    muud = {}
    muu = set()
    for el in tekst:
        if el in täis:
            if el not in täish:
                täish[el] = 1
            else:
                täish[el] += 1
        elif el in kaas:
            if el not in kaash:
                kaash[el] = 1
            else:
                kaash[el] += 1
        else:
            if el not in muud:
                muud[el] = 1
            else:
                muud[el] += 1
    for i in täish:
        k = (i, (täish[i]))
        täishäälikud.add(k)
    for i in kaash:
        k = (i, (kaash[i]))
        kaashäälikud.add(k)
    for i in muud:
        k = (i, (muud[i]))
        muu.add(k)
    tagasta['Täishäälikud'] = täishäälikud
    tagasta['Kaashäälikud'] = kaashäälikud
    tagasta['Muud'] = muu
    return tagasta