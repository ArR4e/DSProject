def seosta_lapsed_ja_vanemad(lapsed,nimed):
    koodid=open(lapsed,encoding='UTF8')
    nimed=open(nimed,encoding='UTF8')
    sõnastik={}
    vanemad={}
    nimi={}
    for rida in koodid:
        rida=rida.strip('\n').split()
        if rida[1] in vanemad:
            vanemad[rida[1]]=str(vanemad[rida[1]])+', '+str(rida[0])
        else:
            vanemad[rida[1]]=rida[0]

    for rida in nimed:
        rida=rida.strip('\n').split()
        täisnimi=rida[:]
        täisnimi.remove(rida[0])
        nimi[rida[0]]=' '.join(täisnimi)
        
    for laps in vanemad:
        lapsenimi=nimi[laps]
        lapsevanem=vanemad[laps].split(', ')
        lapsevanemad=set()
        for inimene in lapsevanem:
            vanemanimi=nimi[inimene]
            lapsevanemad.add(vanemanimi)
        sõnastik[lapsenimi]=lapsevanemad

    koodid.close()
    nimed.close()
    return sõnastik

for vanemlus in seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"):
    lapsevanemad=[]
    for vanem in seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")[vanemlus]:
        lapsevanemad.append(vanem)
    lapsevanemad=', '.join(lapsevanemad)
        
    print(vanemlus+': '+lapsevanemad)
