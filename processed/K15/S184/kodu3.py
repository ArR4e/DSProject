from datetime import datetime

fail=input("Mis on faili nimi?")
f=open(fail, encoding="utf-8")
bussid=[]
hind=0
kestvus=0

for read in f:
    buss=()
    rida=read.strip("\n").split(" ")
    buss=rida
    bussid.append(buss)
    if hind<float(rida[2]):
       hind=int(rida[2])
    väljumine, saabumine=rida[0], rida[1]
    kestvus1= datetime.strptime(saabumine,'%H:%M')-datetime.strptime(väljumine, '%H:%M')
    sekund=kestvus1.total_seconds()
    tundides=sekund/3600
    if kestvus<tundides:
        kestvus=tundides

for i in bussid:
    if str(hind) in i:
        bussid.remove(i)
        
for j in bussid:
    kestvus2= datetime.strptime(j[1],'%H:%M')-datetime.strptime(j[0], '%H:%M')
    sekund=kestvus2.total_seconds()
    tundides=sekund/3600
    if kestvus==tundides:
        bussid.remove(j)
bussid.sort()
f.close()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in bussid:
    print(i[0]+" "+i[1]+" "+i[2])