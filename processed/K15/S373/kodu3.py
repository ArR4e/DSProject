sisestus = input("Sisesta failinimi: ")
järjend = []
fail = open(sisestus, encoding="UTF-8")
for rida in fail.readlines():
    andmed = ((rida.strip().split(" ", 3)))
    järjend.append(andmed)
for i in range(2):
    for buss1 in järjend:
        for buss2 in järjend:
            if buss1 != buss2:
                if buss1[0] > buss2[0]:
                    if buss1[1] < buss2[1]:
                        if int(buss1[2]) < int(buss2[2]):
                            järjend.remove(buss2)
järjend.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for el in järjend:
    bussiajad = el[0] + " " + el[1] + " " + el[2]
    print(bussiajad)
