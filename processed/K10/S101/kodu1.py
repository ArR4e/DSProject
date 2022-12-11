def erinevad_sümbolid(x):
    n=set(x)
    return(n)

def sümbolite_sagedus(x):
    sümbolid=([c for c in x])
    sõnastik={}
    for i in sümbolid:
        n=sümbolid.count(i)
        sõnastik[i]=n
    return(sõnastik)

def grupeeri(x):
    sümbolid=([c for c in x])
    sõnastik={}
    th="aeiouõäöü"
    kh="dfcbghjklmnpqrstvwxyz"
    täishäälik=set()
    kaashäälik=set()
    muu=set()
    
    
    sagedus=sümbolite_sagedus(x)
    
    for i in sagedus:
        if i.lower() in th:
            m=(i,sagedus[i])
            täishäälik.add(m)
        elif i.lower() in kh:
            m=(i,sagedus[i])
            kaashäälik.add(m)
        else:
            m=(i,sagedus[i])
            muu.add(m)
    sõnastik["Täishäälikud"]=täishäälik
    sõnastik["Kaashäälikud"]=kaashäälik
    sõnastik["Muud"]=muu
    
    return(sõnastik)