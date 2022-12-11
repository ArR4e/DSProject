f = open(input('Sisesta faili nimi: '), encoding ='utf-8')
print("Esimesest linnast teise sõitmiseks võiksid kasutada järgmisi busse: ")
bussid=[]
for rida in f:
    uusrida = rida.strip().split(' ')
    bussid.append(uusrida)
bussid.sort()
def sort(bussid):
    for i in range(len(bussid)-1):
        if bussid[i][1] > bussid[i+1][1] and int(bussid[i][2]) > int(bussid[i+1][2]):
            del bussid[i]
            sort(bussid)
            break
sort(bussid)
uusbuss = bussid
uusbuss.sort()
for i in range(len(uusbuss)):
    print(uusbuss[i][0], uusbuss[i][1], uusbuss[i][2])