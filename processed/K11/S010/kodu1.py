def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    f1=open(lastefail, encoding='utf-8')
    f2=open(nimedefail, encoding='utf-8')
    f1_vanematekoodid=[]
    f1_lastekoodid=[]
    for rida in f1:
        andmed1=rida.strip().split()
        f1_vanematekoodid+=[andmed1[0]]
        f1_lastekoodid+=[andmed1[1]]
    f1.close()
    f2_isikukoodid=[]
    f2_nimed=[]
    for rida in f2:
        andmed2=rida.strip().split(' ', 1)
        f2_isikukoodid+=[andmed2[0]]
        f2_nimed+=[andmed2[1]]
    f2.close()
    d2_isikukood_nimi={}
    for indeks in range(len(f2_isikukoodid)):
        d2_isikukood_nimi[f2_isikukoodid[indeks]]=f2_nimed[indeks]  
        
    tulemussõnastik={}
    for indeks in range(len(f1_vanematekoodid)):
        if d2_isikukood_nimi[f1_lastekoodid[indeks]] not in tulemussõnastik:
            tulemussõnastik[d2_isikukood_nimi[f1_lastekoodid[indeks]]]=set()
            tulemussõnastik[d2_isikukood_nimi[f1_lastekoodid[indeks]]].add(d2_isikukood_nimi[f1_vanematekoodid[indeks]])
        else:
            tulemussõnastik[d2_isikukood_nimi[f1_lastekoodid[indeks]]].add(d2_isikukood_nimi[f1_vanematekoodid[indeks]])
    return tulemussõnastik
sõnastik=seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for võti in sõnastik:
    if len(sõnastik[võti])==2:
        vanemad=[]
        for el in sõnastik[võti]:
            vanemad+=[el]
        print(võti+': '+vanemad[0]+', '+vanemad[1])
    else:
        vanem=''
        for el in sõnastik[võti]:
            vanem=el
        print(võti+': '+vanem )