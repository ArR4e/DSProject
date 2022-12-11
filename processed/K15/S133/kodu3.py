fail=input("Sisesta failinimi: ")
#fail="sõiduplaan.txt"
sõiduplaan=open(fail)
kõik=[]
for rida in sõiduplaan:
    k=[]
    a=rida.split(" ")
    a[2]=a[2].strip() 
    k.append(str(a[0]))
    k.append(str(a[1]))
    k.append(str(a[2]))
    kõik.append(str(k[0]) + " " +str(k[1]) + " " + str(k[2]))


    
#print(kõik)

sobiv=[]
m=100000
väikseim_kulu=1000


for i in range(len(kõik)):
    s=1
    n=kõik[i].split()
    for j in range(len(kõik)):
        if kõik[i] not in sobiv:
            k=kõik[j].split()
            varadus=1
            hilisus=1
            raha=1
            if n[0]<k[0]:
                varadus=0
            if n[1]>k[1]:
                hilisus=0
            if int(n[2])>int(k[2]):
                raha=0
            if hilisus==0 and varadus==0 and raha==0:
                s=0
    if s==1:
        sobiv.append(kõik[i])

#print(sobiv)
for i in range(len(sobiv)):
    for j in range(i,len(sobiv)):
        if sobiv[i].split()[0]>sobiv[j].split()[0]:
            sobiv[i],sobiv[j]=sobiv[j],sobiv[i]
        

#print(sobiv)
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in range(len(sobiv)):
    print(sobiv[i])
