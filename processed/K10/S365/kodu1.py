from string import*

sõne = "hulk ei sisalda kunagi korduvaid elemente333"

def erinevad_sümbolid(sõne):
    a = set(sõne)
    return a
def sümbolite_sagedus(sõne):
    b = {}
    for täht in sõne:
        if täht in b:
            b[täht] = b[täht]+1
        else:
            b[täht] = 1
    return b
def grupeeri(sõne):
    täishäälikud=('A','a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü')
    täis_hulk = set()
    kaashäälikud = ('L','K','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w','y')
    kaas_hulk = set()
    muud = set()
    märgid = list(punctuation)
    teised = ['0','1','2','3','4','5','6','7','8','9',' ']
    märgid = märgid + teised
    for täht in täishäälikud:
        k = 0
        for m in sõne:
            if m == täht:
                k += 1
            else:
                continue
        if k>0:
            täis_hulk.add((täht, k))
    for täht in kaashäälikud:
        k = 0
        for m in sõne:
            if m == täht:
                k += 1
            else:
                continue
        if k>0:
            kaas_hulk.add((täht, k))
    for täht in märgid:
        k=0
        for m in sõne:
            if m == täht:
                k+=1
            else:
                continue
        if k>0:
            muud.add((täht, k))


    s= {}
    s['Täishäälikud'] = täis_hulk
    s['Kaashäälikud'] = kaas_hulk
    s['Muud'] = muud
    return s
        

print(erinevad_sümbolid(sõne))
print(sümbolite_sagedus(sõne))
print(grupeeri(sõne))

    