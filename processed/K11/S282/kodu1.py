def seosta_lapsed_ja_vanemad(lapsed,nimed):
    lapsed=open(lapsed)
    nimed=open(nimed)
    sonastik_lapsed={}
    sonastik_nimed={}
    sonastik_vanemad={}
    for rida in lapsed:
        hulk_lapsed=set()
        list_lapsed=rida.strip().split()
        if list_lapsed[1] in sonastik_lapsed:
            sonastik_lapsed[list_lapsed[1]].add(list_lapsed[0])
        else:
            hulk_lapsed.add(list_lapsed[0])
            sonastik_lapsed[list_lapsed[1]]=hulk_lapsed
    for rida in nimed:
        list_nimed=rida.strip().split()
        sonastik_nimed[list_nimed[0]]=''.join(list_nimed[1]+' '+list_nimed[2])
    for el in sonastik_lapsed:
        hulk_nimed=set()
        for i in sonastik_lapsed[el]:
            hulk_nimed.add(sonastik_nimed[i])
        sonastik_vanemad[sonastik_nimed[el]]= hulk_nimed
    lapsed.close()
    nimed.close()
    return sonastik_vanemad

sonastik=seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt')

for el in sonastik:
    print(el+': '+', '.join(sonastik[el]))