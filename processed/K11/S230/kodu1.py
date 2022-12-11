def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f=open(lapsed) 
    s={}
    for i in f:
        i=i.split()
        i[0]=nimi(i[0],nimed)
        i[1]=nimi(i[1],nimed)
        try:s[i[1]]={i[0], s[i[1]]}
        except:s[i[1]]=i[0]
    for i in s:
        try:s[i]={s[i]}
        except:
            continue
    f.close()
    return s
    
def nimi(kood,nimed):
        f=open(nimed, encoding="UTF-8")
        for a in f:
            a=a.split()
            if kood == a[0]:
                f.close()
                return a[1]+" "+a[2]
    
s=seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for i in s:
    print(i, end=": ")
    a=list(s[i])
    if len(s[i])==2:
        print(f"{a[0]}, {a[1]}")
    else:
        print(a[0])