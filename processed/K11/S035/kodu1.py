def seosta_lapsed_ja_vanemad(lapsed, nimed):
    sõnastik={}
    inimesed={}
    f=open(lapsed)
    g=open(nimed)
    for line in g:
        b=line.split()
        inimesed[b[0]]=b[1] + " " + b[2]
    for rida in f:
        a=rida.split()
        if inimesed[a[1]] not in sõnastik:
            vanemad=set()
            vanemad.add(inimesed[a[0]])
            sõnastik[inimesed[a[1]]]=vanemad
        else:
            vanemad=(sõnastik[inimesed[a[1]]])
            vanemad.add(inimesed[a[0]])
            sõnastik[inimesed[a[1]]]=vanemad
    return(sõnastik)
lapsed_vanemad=seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for võti in lapsed_vanemad:
    vanemate_nimed=lapsed_vanemad[võti]
    if len(vanemate_nimed)>1:
        vanemate_nimed=", ".join(vanemate_nimed)
    else:
        vanemate_nimed="".join(vanemate_nimed)
    print(võti + ": " + vanemate_nimed)