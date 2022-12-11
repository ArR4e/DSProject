lapsed='lapsed.txt'
nimed='nimed.txt'

def seosta_lapsed_ja_vanemad(lapsed,nimed):
    lapsed=open(lapsed)
    nimed=open(nimed)
    kood_nimeks={}
    for rida in nimed:
        rida=rida.strip().split(' ')
        kood_nimeks[rida[0]]=' '.join(rida[1:])
    lapsed_maatriks=[]
    for rida in lapsed:
        rida=rida.strip().split()
        lapsed_maatriks+=[rida]
    for x in lapsed_maatriks:
        i=0
        for y in x:
            for a in kood_nimeks:
                if y==a:
                    x[i]=kood_nimeks[a]
            i+=1
    lapsed_vanemad={}
    for x in lapsed_maatriks:
        if x[1] not in lapsed_vanemad:
            lapsed_vanemad[x[1]]={x[0]}
        else:
            lapsed_vanemad[x[1]].add(x[0])
    return lapsed_vanemad


lapsed_vanemad=seosta_lapsed_ja_vanemad(lapsed,nimed)
lapsed=lapsed_vanemad.keys()
for laps in lapsed:
    print(laps+ ': '+ ', '.join(lapsed_vanemad[laps]))


