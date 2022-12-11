def erinevad_sümbolid(a):
    sumbolid = set()
    #b = a.split()
    for sumbol in a:
        if sumbol not in sumbolid:
            sumbolid.add(sumbol)
    return sumbolid


#erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
def sümbolite_sagedus(a):
    sagedus = {}
    for sumbol in a:
        sagedus[sumbol] = sagedus.get(sumbol, 0) + 1
    return sagedus

#sümbolite_sagedus("Hei hopsti, väikevend!")
    
def grupeeri(a):
    tais = set()
    kaas = set()
    sumb = set()
    koond = {}
    sagedus = sümbolite_sagedus(a)
    sagedus1 = list(sagedus.keys())
    for sumbol in sagedus1:
        if sumbol.lower() in "aeiouõüöä":
            esimene = sumbol 
            teine = sagedus[sumbol]
            kolmas = (esimene, teine)
            tais.add(kolmas)
        if sumbol.lower() in "qwrtypsdfghjklmnbvcxz":
            esimene = sumbol
            teine = sagedus[sumbol]
            kolmas = (esimene, teine)
            kaas.add(kolmas)
        if sumbol.lower() not in "aeiouõüöäqwrtypsdfghjklmnbvcxz":
            esimene = sumbol
            teine = sagedus[sumbol]
            kolmas = (esimene, teine)
            sumb.add(kolmas)
    koond["Täishäälikud"] = tais
    koond['Kaashäälikud'] = kaas
    koond['Muud'] = sumb
    return koond

grupeeri("sõida tasa üle silla")