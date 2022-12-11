fail=input("Sisesta failinimi: ")
f=open(fail)
ajad=[]
eemalda=[]

for i in f:
    i=i.split()
    ajad+=[i]

for i in ajad:
    for j in range(len(ajad)):
        if int("".join(i[0].split(":")))<int("".join(ajad[j][0].split(":"))) and int("".join(i[1].split(":")))>int("".join(ajad[j][1].split(":"))) and int(i[2])>int(ajad[j][2]):
            if i not in eemalda:
                eemalda+=[i]
                
for i in eemalda:
    ajad.remove(i)
    
for i in range(len(ajad)):
    for j in range(len(ajad)):
        if int("".join(ajad[i][0].split(":")))<int("".join(ajad[j][0].split(":"))):
            ajad[i],ajad[j]=ajad[j],ajad[i]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in range(len(ajad)):
    print(ajad[i][0],ajad[i][1],ajad[i][2])