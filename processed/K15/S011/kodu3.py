fail = str(input("Sisesta failinimi: ")) #sõiduplaan.txt
f = open(fail)
read = f.readlines()
f.close()
väljumine=[]
saabumine=[]
hind=[]

# haki read nii et oleks eraldi järjendites väljumine, saabumine, hind
for rida in read:
    info = rida.split(" ")
    väljumine.append(info[0])
    saabumine.append(info[1])
    hind.append((info[-1]).strip('\n'))
#funktsioon mis leiab sobivaimad bussiajad ja väljastab need
def sobivaim(väljumine, saabumine, hind):
    for el in hind:
        if el == max(hind):
            indeks = hind.index(el)
            väljumine.pop(indeks)
            saabumine.pop(indeks)
            hind.pop(indeks)
    for el in väljumine:
        if el == max(väljumine):
            indeks = väljumine.index(el)
            väljumine.pop(indeks)
            saabumine.pop(indeks)
            hind.pop(indeks)
    for el in saabumine:
        if el == max(saabumine):
            indeks = saabumine.index(el)
            väljumine.pop(indeks)
            saabumine.pop(indeks)
            hind.pop(indeks)

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
sobivaim(väljumine, saabumine, hind)
sobivaid = len(hind)
x = sobivaid
while x >= 0:
    print(str(väljumine[x-1]) + " " +str(saabumine[x-1]) +" " + str(hind[x-1]))
    x -= 1