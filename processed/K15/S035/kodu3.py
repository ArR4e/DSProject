fail=input("Sisesta failinimi: ")
f=open(fail)
järjend=[]
eemaldamiseks=[]
for rida in f:
    järjend.append(rida.replace("\n", ""))
for i in järjend:
    eraldi=i.split()
    for j in järjend:
        eraldi2=j.split()
        if eraldi[0]<eraldi2[0] and eraldi[1]>eraldi2[1] and int(eraldi[2])>int(eraldi2[2]):
            eemaldamiseks.append(i)
            break
for elem in eemaldamiseks:
    järjend.remove(elem)
for a in range(len(järjend)):
    min=a
    for b in range(a+1, len(järjend)):
        o=järjend[b].split()
        p=järjend[min].split()
        if o[0]<p[0]:
            min=b        
    if a!=min:
        järjend[a], järjend[min] = järjend[min], järjend[a]
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for elem in järjend:
    print(elem)