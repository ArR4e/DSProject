from datetime import datetime as dt #selle mooduliga saab aegu paremini võrrelda

#kogu koodi oleks saanud teha ka poole lühemaks korduvate tsüklite arvelt,aga jäi tegemata

failinimi=input('Sisesta failinimi: ')
f=open(failinimi, encoding= 'UTF-8')
#f=open('sõiduplaan.txt', encoding= 'UTF-8')

t1='09:00'
t2='11:30'
kell1=dt.strptime(t1,'%H:%M')
kell2=dt.strptime(t2,'%H:%M')
vahe= kell2- kell1
vahe=vahe.total_seconds()/3600

#loeme info sisse ja salvestame järjendisse
sõiduplaan=[]
for rida in f:
    info= rida.strip('\n').split(' ')
    sõiduplaan.append(info)
f.close()

#leiame sõidu kestused
for buss in sõiduplaan:
    väljumine= dt.strptime(buss[0], '%H:%M')
    saabumine= dt.strptime(buss[1], '%H:%M')
    vahe= saabumine- väljumine
    vahe=vahe.total_seconds()/3600 #teeme tundideks
    buss.append(vahe)

#valides saab olla kaks miinust , kas kallim hind kui kõige odavam või pikem aeg kui kõige lühem

#leiame lühima sõidukestuse
for kestus in sõiduplaan:
    lühike=100
    if kestus[3]< lühike:
        lühike= kestus[3]

#leiame odavaima hinna
for hind in sõiduplaan:
    odavaim=100
    if float(hind[2])< odavaim:
        odavaim= float(hind[2])

for buss in sõiduplaan:
    n=0
    if float(buss[2])> odavaim:
        n+=1
    if buss[3]> lühike:
        n+=1
    buss.append(n)
    
#nüüd eraldame sobivad bussiajad teistest

sobiv_sõiduplaan=[]

for buss in sõiduplaan:
    if buss[4] < 2:
        sobiv_sõiduplaan.append(buss)
        
#järjestame väljumisaegade järgi
        

for i in range(len(sobiv_sõiduplaan)):
    min = i 
    for j in range(i+1, len(sobiv_sõiduplaan)):
        if int(sobiv_sõiduplaan[j][0].replace(':','')) < int(sobiv_sõiduplaan[min][0].replace(':','')):
            min = j
    if i != min: 
        sobiv_sõiduplaan[i], sobiv_sõiduplaan[min] = sobiv_sõiduplaan[min], sobiv_sõiduplaan[i] 

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')
print()
print('väljub\t saabub\t hind')

for buss in sobiv_sõiduplaan:
    print('\t '.join(buss[:3]))
    