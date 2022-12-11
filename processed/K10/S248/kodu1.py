def erinevad_sümbolid(x):
    y=set()
    for i in x:
        y.add(i)
    return y

def sümbolite_sagedus(x):
    y={}
    m=0
    for i in x:
        m=x.count(i)
        y[i]=m
    return y

def grupeeri(x):
    y={}
    th=set()
    kh=set()
    mh=set()
    m=0
    for i in x:
        if i in "aeiouõäöüAEIOUÕÄÖÜ":
            m=x.count(i)
            v=(i,m)
            th.add(v)
        elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            m=x.count(i)
            v=(i,m)
            kh.add(v)
        else:
            m=x.count(i)
            v=(i,m)
            mh.add(v)
    
    y["Täishäälikud"]=th
    y["Kaashäälikud"]=kh
    y["Muud"]=mh
    return y




        
    
