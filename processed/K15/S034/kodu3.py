from datetime import datetime
format = '%H:%M'
faili_nimi = input('Sisesta faili nimi: ')
#faili_nimi = 'sõiduplaan.txt'
f = open(faili_nimi)
read = f.readlines()
listike = [] 
listikeU = []
loendur = 0
sõnastik = {}
sõnastik2 = {}
for rida in read:
    listikeU.append(rida.split()) 
listike = sorted(listikeU)


for rida in read: 
    loendur +=1
    väljumine = listike[loendur-1][0]
    saabumine = listike[loendur-1][1]
    sõidu_pikkus = str(datetime.strptime(saabumine,format) - datetime.strptime(väljumine,format))
    sõnastik[loendur-1] = sõidu_pikkus
    sõnastik2[loendur-1] = listike[loendur-1][2] 



sobivad_liikmed = []
kas_esimene = 0
for indeks,aeg in sõnastik.items():
    if kas_esimene == 0:
        kas_esimene +=1
        vähim_aeg = aeg
        sobivad_liikmed.append(indeks)
    else:
        if aeg <= vähim_aeg:
            if aeg < vähim_aeg:
                vähim_aeg =aeg
                sobivad_liikmed = []
                sobivad_liikmed.append(indeks)
            else:
                vähim_aeg = aeg
                sobivad_liikmed.append(indeks)

    
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')

for element in sobivad_liikmed:
    print(' '.join(listike[element]))


f.close()