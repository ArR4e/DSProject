fail = open(input("Sisesta failinimi: "), "r", encoding="utf-8")

tekst = fail.readlines()

bussid = {}

n = 0

for rida1 in tekst:
    sobib = True
    for rida2 in tekst:
        if rida1.split()[0] < rida2.split()[0]:
            if rida1.split()[1] > rida2.split()[1]:
                if float(rida1.split()[2]) > float(rida2.split()[2]):
                    sobib = False
    if sobib == True:
        aeg1 = rida1.split()[0]
        aeg2 = rida1.split()[1]
        hind = rida1.split()[2].replace("\n", "")
        bussid[str(n)] = [aeg1, aeg2, hind]
        n+=1
    
muudatused = 1

while muudatused != 0:
    muudatused = 0
    for indeks in range(len(bussid)-1):
        indeks = str(indeks)
        if bussid[indeks][0] > bussid[str(int(indeks)+1)][0]:
            buss1 = bussid[indeks]
            buss2 = bussid[str(int(indeks)+1)]
            bussid[indeks] = buss2
            bussid[str(int(indeks)+1)] = buss1
            muudatused = 1

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for b_number in bussid:
    print(bussid[b_number][0],bussid[b_number][1],bussid[b_number][2])