#failinimi = input("Sisesta failinimi: ")
failinimi= "sõiduplaan.txt"
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

f = open(failinimi,"r")
sisu = f.readlines()
test = []
for i in sisu:
    i = i.replace("\n","").split(" ")
    test.append(i)
f.close()

sobivad_bussid = []
sobivad_bussid.append(test[0])
print(sobivad_bussid)
for i in test:
    #print(i)
    for j in test:
       print(j)
        #print(i[1])
    