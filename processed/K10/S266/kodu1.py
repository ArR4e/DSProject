def erinevad_sümbolid(tekst):
    symbolid = set(tekst)
    return symbolid

def sümbolite_sagedus(tekst):
    sagedus = {}
    for arv in tekst:
        sagedus[arv] = sagedus.get(arv, 0) + 1
    return sagedus
#sümbolite_sagedus("Hei hopsti, väikevend!")

def grupeeri(tekst):
    taishaalikud = ('a', 'e', 'i','o' ,'u', 'õ', 'ä', 'ö', 'ü',
                    'A', 'E', 'I','O' ,'U', 'Õ', 'Ä', 'Ö', 'Ü')
    kaashaalikud = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 'q', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y',
                    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'Q', 'S', 'Š', 'Z', 'Ž', 'T', 'V', 'W', 'X', 'Y')
    grupeering = {}
    grupeering['Täishäälikud'] = set()
    grupeering['Kaashäälikud'] = set()
    grupeering['Muud']         = set()
    
    sagedus = sümbolite_sagedus(tekst)
    for k in sagedus.items():
        if k[0] in taishaalikud:
            grupeering['Täishäälikud'].add(k)
        elif k[0] in kaashaalikud:
            grupeering['Kaashäälikud'].add(k)
        else:
             grupeering['Muud'].add(k)
    return grupeering

#grupeeri('sõida tasa üle silla')    