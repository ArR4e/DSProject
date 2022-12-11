nimedefailinimi='nimed.txt'
lastefailinimi='lapsed.txt'
def seosta_lapsed_ja_vanemad(lastefailinimi,nimedefailinimi):
    f1=open(nimedefailinimi, encoding='UTF-8')
    nimed=[]
    for rida in f1:
        rida=rida.strip().split(' ')
        nimed.append(rida)
    f1.close()
    f2=open(lastefailinimi,encoding='UTF-8')
    lapsed=[]
    for rida in f2:
        rida=rida.strip().split(' ')
        lapsed.append(rida)
    f2.close()
    isikukood_ja_nimi={}
    perekond={}
    for rida in nimed:
        isikukood_ja_nimi[(rida[0])]=rida[1]+' ' +rida[2]
    for rida in lapsed:
        if isikukood_ja_nimi[(rida[1])] in perekond:
            perekond[isikukood_ja_nimi[(rida[1])]].add(isikukood_ja_nimi[(rida[0])])
        else:
            perekond[isikukood_ja_nimi[(rida[1])]]=set()
            perekond[isikukood_ja_nimi[(rida[1])]].add(isikukood_ja_nimi[(rida[0])])
    return perekond
sõnastik=seosta_lapsed_ja_vanemad(lastefailinimi,nimedefailinimi)
vanemad=[]
for võti in sõnastik:
    if len(sõnastik[võti]) == 2:
        for i in sõnastik[võti]:
            vanemad.append(i)
        print(võti+': '+vanemad[0]+', '+vanemad[1])
        vanemad=[]
    else:
        for i in sõnastik[võti]:
            vanemad.append(i)
            print(võti+': '+ vanemad[0])
            vanemad=[]