f=open(input(str("Sisesta failinimi: ")))
# f=open("sõiduplaan.txt")
a=[]
for line in f:
    a+=[line.strip().split(" ")]

ajad=[]
for i in range(len(a)):
    ajad+=[int(a[i][1].split(":")[0])*60+int(a[i][1].split(":")[1])-int(a[i][0].split(":")[0])*60-int(a[i][0].split(":")[1])]

x=len(a)
for z in range(x):
    try:
        for i in range(len(a)):
            for j in range(len(a)):
                if (ajad[i]>ajad[j] and int(a[i][2])>int(a[j][2])):
                    a.pop(i)
                    ajad.pop(i)
                    
    except:
        True

f.close()

for i in range(len(a)):
    for j in range(i,len(a)):
        if int(a[i][0].split(":")[0])*60+int(a[i][0].split(":")[1]) > int(a[j][0].split(":")[0])*60+int(a[j][0].split(":")[1]):
            a[i],a[j],ajad[i],ajad[j]=a[j],a[i],ajad[j],ajad[i]
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in a:
    for j in i:
        print(j,end=" ")
    print()