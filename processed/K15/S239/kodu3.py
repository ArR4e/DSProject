failinimi=input("Palun sisesta faili nimi: ")
f=open(failinimi)

sobimatu=set()
for rida1 in f:
    rida1=rida1.split()
    aeg1=int((rida1[1].split(":"))[0])*60-int((rida1[0].split(":"))[0])*60+int((rida1[1].split(":"))[1])-int((rida1[0].split(":"))[1])
    for rida2 in f:
        rida2=rida2.split()
        aeg2=int((rida2[1].split(":"))[0])*60-int((rida2[0].split(":"))[0])*60+int((rida2[1].split(":"))[1])-int((rida2[0].split(":"))[1])
        if aeg2>aeg1:
            if int(rida2[2])>int(rida1[2]):
                sobimatu.add(str(rida2))

faili_sisu=f.readlines()
for i in sobimatu:
    faili_sisu.remove(i)
for i in range(len(faili_sisu)-1,0,-1):
    for j in range(i):
        if int((faili_sisu[j].split()[0]).split(":")[0])*60>int((faili_sisu[j+1].split()[0]).split(":")[0])*60:
            x=faili_sisu[j]
            faili_sisu[j]=faili_sisu[j+1]
            faili_sisu[j+1]=x
        elif int((faili_sisu[j].split()[0]).split(":")[1])>int((faili_sisu[j+1].split()[0]).split(":")[1]):
            if int((faili_sisu[j].split()[0]).split(":")[1])>int((faili_sisu[j+1].split()[0]).split(":")[1]):
                x=faili_sisu[j]
                faili_sisu[j]=faili_sisu[j+1]
                faili_sisu[j+1]=x


print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in faili_sisu:
    print(i)

f.close()