failinimi=input("Sisesta failinimi: ")
#failinimi="bussid.txt"
f=open(failinimi)
bussid=[]
for rida in f:
    rida=rida.strip("\n").split(" ")
    väljumine=rida[0]
    saabumine=rida[1]
    hind=rida[2]
    ennik=(väljumine,saabumine,hind)
    bussid.append(ennik)
for buss in range(len(bussid)):
    min=buss
    for teine in range(buss+1,len(bussid)):
        if int(bussid[teine][2])<int(bussid[min][2]) :
                min=teine
        if buss != min:
            bussid[buss],bussid[min]=bussid[min],bussid[buss]
for i in range(len(bussid)):
    for j in range(i+1,len(bussid)):
        if bussid[j][2]==bussid[i][2]:
            if bussid[j][0]>bussid[i][0] and bussid[j][1]<bussid[i][1]:
                #bussid.remove(bussid[j])
                bussid[i],bussid[j]=bussid[j],bussid[i]
#Kellaaegade sortimisega mingi jama
#Sprint(bussid)
#Nüüd oleks vaja võrrelda veelkord kellaaegu ja elimineerida
#liiga pikad sõiduajad. Seejärel valida hinna järgi(?) parimad bussid 

f.close()
