
def erinevad_sümbolid(sõne):
    x=set(sõne)
    return x


def sümbolite_sagedus(sõne):
    d={}
    järjend=list(sõne)
    for täht in järjend:
        d[täht]=d.get(täht,0)+1
    return(d)


def grupeeri(sõne):
    Täis="aeiouöäüõAEIOUÖÄÜÕ"
    kaas="kptgbdhjlmnrsvfcxyqzwKPTGBDHJLMNRSVFCXYQZW"
    d={}
    t={}
    k={}
    m={}
    th=set()
    kh=set()
    mh=set()
    leitudtäis= set(Täis) & set(sõne)
    leitudkaas= set(kaas) & set(sõne)
    muu=set(sõne) - set(Täis) - set(kaas)
    for i in sõne:
        if i in leitudtäis:
            t[i]=t.get(i, 0)+1
    for i in sõne:
        if i in leitudkaas:
            k[i]=k.get(i, 0)+1
            
    for i in sõne:
        if i in muu:
            m[i]=m.get(i, 0)+1
            
    for i in t:
        th.add((i, t[i]))
    for i in k:
        kh.add((i, k[i]))
    for i in m:
        mh.add((i, m[i]))
        
    d["Täishäälikud"]=th
    d["Kaashäälikud"]=kh
    d["Muud"]=mh
    return(d)
            
#print(grupeeri("sõida tasa üle silla!"))