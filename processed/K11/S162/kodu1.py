def seosta_lapsed_ja_vanemad(lapsed,nimed):
    inimesed={}
    tulemus={}
    with open(nimed) as file:
        for rida in file:
            rida=rida.strip().split(None,1)
            inimesed[rida[0]]=rida[1]
    with open(lapsed) as file:
        for rida in file:
            rida=rida.strip().split()
            vanem=rida[0]
            laps=rida[1]
            if inimesed[laps] not in tulemus:
                tulemus[inimesed[laps]]=set()
                tulemus[inimesed[laps]].add(inimesed[vanem])
            else:
                tulemus[inimesed[laps]].add(inimesed[vanem])
    return tulemus
sõnastik=seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
for nimi in sõnastik:
    print(nimi,end=': ')
    s=list(sõnastik[nimi])
    if len(sõnastik[nimi])==2:
        print(s[0]+', '+s[1])
    else:
        print(s[0])

