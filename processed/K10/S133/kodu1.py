def erinevad_sümbolid(a):
    sümbolid=set()
    for sõne in a:
        sümbolid.add(sõne)
    return sümbolid
#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(jutt):
    hulk={}
    for asi in jutt:
        if asi not in hulk:
            hulk[asi]=1
        elif asi in hulk:
            hulk[asi]=hulk[asi]+1
    return hulk
#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(lause):
    hulk={}
    hulk['Täishäälikud']={}
    hulk['Kaashäälikud']={}
    hulk['Muud']={}
    tä=[]
    ka=[]
    mu=[]
    täi=set()
    kaa=set()
    muu=set()
    täishäälikud=[ "a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaashäälikud=["c","b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "š", "z", "ž", "t", "v", "q","x","w","y"]
    for asi in lause:
        if asi.lower() in täishäälikud:
            if asi not in tä:
                tä.append(asi)
                tä.append("1")
            elif asi in tä:
                tä[tä.index(asi)+1]=str(int(tä[tä.index(asi)+1])+1)
        elif asi.lower() in kaashäälikud:
            if asi not in ka:
                ka.append(asi)
                ka.append("1")
            elif asi in ka:
                ka[ka.index(asi)+1]=str(int(ka[ka.index(asi)+1])+1)
        else:
            if asi in mu:
                mu[mu.index(asi)+1]=str(int(mu[mu.index(asi)+1])+1)
            elif asi not in mu:
                mu.append(asi)
                mu.append("1")
    i=0
    while i<len(tä):
        täi.add((tä[i],int(tä[i+1])))
        i+=2
    i=0
    while i<len(ka):
        kaa.add((ka[i],int(ka[i+1])))
        i+=2
    i=0
    while i<len(mu):
        muu.add((mu[i],int(mu[i+1])))
        i+=2
    hulk['Täishäälikud']=täi
    hulk['Kaashäälikud']=kaa
    hulk['Muud']=muu
    return hulk
print(grupeeri("kuu-uurija"))