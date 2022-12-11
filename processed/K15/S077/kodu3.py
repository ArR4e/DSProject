fnimi=input("Sisesta faili nimi: ")
f=open(fnimi,encoding="UTF-8")

read=f.readlines()

üleliigsed=set()
for el in read:
    for el2 in read:
        if read.index(el)!=read.index(el2):
            if int(el[12:])>=int(el2[12:]):
                if int(el[0:2])<int(el2[0:2]) and int(el[6:8])>int(el2[6:8]) or\
                (int(el[0:2])==int(el2[0:2]) and int(el[6:8])>int(el2[6:8]) and int(el[3:5])<=int(el2[3:5])) or\
                (int(el[0:2])<int(el2[0:2]) and int(el[6:8])==int(el2[6:8]) and int(el[9:11])>=int(el2[9:11])) or\
                (int(el[0:2])==int(el2[0:2]) and int(el[6:8])==int(el2[6:8]) and int(el[3:5])<=int(el2[3:5]) and int(el[9:11])>=int(el2[9:11])):
                    üleliigsed.add(el)

read=set(read)
read-=üleliigsed
read=list(read)

for i in range(len(read)-1):
    for j in range(i+1,len(read)):
        if read[i][0:2]>read[j][0:2] or (read[i][0:2]==read[j][0:2] and read[i][3:5]>read[j][3:5]):
            read[i],read[j]=read[j],read[i]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:\n")
for el in read:
    print(el.replace("\n",""))
        
f.close()