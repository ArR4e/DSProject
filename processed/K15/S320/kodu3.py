def sõiduaeg(algus, lõpp):
    start=algus.split(":")
    algus=int(start[0])+int(start[1])/60
    finish=lõpp.split(":")
    lõpp=int(finish[0])+int(finish[1])/60
    return lõpp-algus

a=input("Sisesta failinimi:")
f=open(a, encoding="utf-8")

bussid=[]
sobivad=[]
for rida in f:
    mõistlikud=[]
    rida=rida.strip().split()
    bussid.append(rida)
f.close()
    
for buss in bussid:
    sobiv=True
    for buss2 in bussid:
        if buss[0]<buss2[0] and sõiduaeg(buss[0], buss[1])>sõiduaeg(buss2[0], buss2[1]) and int(buss[2])>int(buss2[2]):
            sobiv=False
            break
    if sobiv:
        sobivad.append(buss)
 
        

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmiseid busse:")
for sobiv in sorted(sobivad):
    print(" ".join(sobiv))
