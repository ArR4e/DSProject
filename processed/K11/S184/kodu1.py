def seosta_lapsed_ja_vanemad(a,b):
    f=open(a)
    f2=open(b)
    sõnastik={}
    sõnastik2={}
    
    for rida2 in f2:
        isik=rida2.split()
        if len(isik)>1:
            isikukood=isik[0]
            nimi=isik[1]+" "+ isik[2]
            sõnastik[isikukood]=nimi
            
    for rida in f:
        seotud=rida.split()
        if len(seotud)>1:
            vanem=seotud[0]
            laps=seotud[1]
            nimi_vanem= sõnastik[vanem]
            nimi_laps= sõnastik[laps]
            
        if nimi_laps not in sõnastik2:
            sõnastik2[nimi_laps]=set()
            sõnastik2[nimi_laps].add(nimi_vanem)
        else:
            sõnastik2[nimi_laps].add(nimi_vanem)
    print(sõnastik2)
    return sõnastik2
    f.close()
    f2.close()
  
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")