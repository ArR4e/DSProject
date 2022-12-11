def puhasta(nimekiri):
    for a in range(len(nimekiri)):
        nimekiri[a]=nimekiri[a].strip("\n")
        nimekiri[a]=nimekiri[a].split()
    return(nimekiri)
def seosta_lapsed_ja_vanemad(lastenimi,kõiknimed):
    f=open(lastenimi,encoding="UTF-8")
    lastefail=f.readlines()
    f.close()
    f=open(kõiknimed,encoding="UTF-8")
    nimed=f.readlines()
    f.close()
    puhasta(lastefail)
    puhasta(nimed)
    andmebaas={}
    for rida in nimed:
        pikknimi=[]
        for pikkus in range(len(rida)-1):
            pikknimi.append(rida[pikkus+1])
        pikknimi=" ".join(pikknimi)
        andmebaas[rida[0]]=pikknimi
    for a in range(len(lastefail)):
        lastefail[a][0]=andmebaas[lastefail[a][0]]
        lastefail[a][1]=andmebaas[lastefail[a][1]]
    lapsed={}
    for a in lastefail:
        vanemate_hulk=set()
        for b in lastefail:
            if a[1]==b[1]:
                vanemate_hulk.add(a[0])
                vanemate_hulk.add(b[0])
        lapsed[a[1]]=vanemate_hulk
    return(lapsed)
