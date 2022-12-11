import copy

failinimi=input('Sisesta failinimi: ')
f=open(failinimi, encoding='utf-8')
bussid=[]
for rida in f:
    buss=rida.strip().split(' ')
    bussid+=[buss]
f.close()
print(bussid)

bussid_teisendatud=[]
for buss in bussid:
    aeg1=buss[0].split(':') #väljumine
    teisendatudaeg1=int(aeg1[0])*60+int(aeg1[1]) # aeg minutites
    aeg2=buss[1].split(':')
    teisendatudaeg2=int(aeg2[0])*60+int(aeg2[1])
    aegade_vahe=teisendatudaeg2-teisendatudaeg1
    bussid_teisendatud.append([aegade_vahe, int(buss[2])])
print(bussid_teisendatud)


bussid_teisendatud2=copy.deepcopy(bussid_teisendatud)
def järjesta_punktid(p): # Kasutasin selection sort meetodit ehk valikumeetodit
    for indeks in range(0, len(p)-1):
        #rida=p[indeks][1]
        #veerg=p[indeks][0]
        vähim=indeks
        for j in range(indeks, len(p)):
            if p[j][1]<p[vähim][1]:
                vähim=j
            elif p[j][1]==p[vähim][1] and p[j][0]<p[vähim][0]:
                vähim=j            
        p[indeks], p[vähim]=p[vähim], p[indeks]
    return p
järjesta_punktid(bussid_teisendatud2)
indeksid=[]
for el in bussid_teisendatud2:
    õige_indeks=bussid_teisendatud.index(el)
    indeksid.append(õige_indeks)
print(indeksid)

loendur=0
for i in range(len(bussid)):
    indeks=indeksid[i]
    print(bussid[indeks])
    loendur+=1
    if loendur>=2:
        break
    
# ei jõudnud kahjuks lõpetada, sest ei teadnud, kuidas saada mitu õiget indeksit