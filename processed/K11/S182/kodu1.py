def seosta_lapsed_ja_vanemad(lapsed, nimed):
    isikud={}
    tulemused={}
    with open(nimed)as file:
        for rida in file:
            rida=rida.strip().split(None,1)
            isikud[rida[0]]=rida[1]
    with open(lapsed) as file:
        for rida in file:
            rida=rida.strip().split()
            lapsevanem=rida[0]
            laps=rida[1]
            if isikud[laps] not in tulemused:
                tulemused[isikud[laps]]=set()
                tulemused[isikud[laps]].add(isikud[lapsevanem])
            else:
                tulemused[isikud[laps]].add(isikud[lapsevanem])
    return tulemused

tekst=seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for nimi in tekst:
    print(nimi,end=": ")
    s=list(tekst[nimi])
    if len(tekst[nimi])==2:
        print(s[0]+", "+s[1])
    else:
        print(s[0])