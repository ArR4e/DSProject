def erinevad_sümbolid(sõne):
    leitud=[]
    for märk in sõne:
        if märk not in leitud:
            leitud.append(märk)
    tulemus=set(leitud)
    return tulemus

def sümbolite_sagedus(sõne):
    d={}
    for arv in sõne:
        if arv in d:
            d[arv]=d[arv]+1
        else:
            d[arv]=1
    return d

def grupeeri(sõne):
    vokaalid=('a','e','i','o','u','õ','ä','ö','ü')
    Svokaalid=('A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü')
    kinnised=('b','d','f','g','h','j','k','l','m','n','p','r','s','š','z','ž','t','v','x','y','c','q','w')
    Skinnised=('B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'Š', 'Z', 'Ž', 'T', 'V', 'X', 'Y', 'C', 'Q', 'W')
    t={}
    k={}
    m={}
    for häälik in sõne:
        if häälik in vokaalid or häälik in Svokaalid:
            if häälik in t:
                t[häälik]=t[häälik]+1
            else:
                t[häälik]=1
        elif häälik in kinnised or häälik in Skinnised:
            if häälik in k:
                k[häälik]=k[häälik]+1
            else:
                k[häälik]=1
        else:
            if häälik in m:
                m[häälik]=m[häälik]+1
            else:
                m[häälik]=1
    tlist=[(k, v) for k, v in t.items()]
    klist=[(k, v) for k, v in k.items()]
    mlist=[(k, v) for k, v in m.items()]
    
    valmis={}
    valmis['Täishäälikud']=set(tlist)
    valmis['Kaashäälikud']=set(klist)
    valmis['Muud']=set(mlist)
    return valmis