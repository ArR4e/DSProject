import copy
nimi=input("Sisesta failinimi:")

def aeg(a):
    t=int(a[:2])+int(a[3:])/60
    return t

f=open(nimi, "r")
read=[]
for rida in f:
    rida=rida.strip().split(" ")
    read.append(rida)
    
for i in range(len(read)-1):
    for j in range(i+1, len(read)):
        if aeg(read[i][0])>aeg(read[j][0]):
            read[i],read[j]=read[j],read[i]
        if aeg(read[i][0])==aeg(read[j][0]):
            if aeg(read[i][1])>aeg(read[j][1]):
                read[i],read[j]=read[j],read[i]

read2=copy.deepcopy(read)
for i in read2:
    read3=copy.deepcopy(read)
    for j in read3:
        if i==j:
            continue
        if aeg(i[0])>aeg(j[0]) and aeg(i[1])<aeg(j[1]) and int(i[2])<int(j[2]):
            read.remove(j)
        elif aeg(i[0])==aeg(j[0]) or aeg(i[1])==aeg(j[1]):
            if aeg(i[1])-aeg(i[0])<aeg(j[1])-aeg(j[0]) and int(i[2])<int(j[2]):
                read.remove(j)
                




print(" Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in read:
    print(" ".join(i))


f.close