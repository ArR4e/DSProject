failinimi = input("Sisesta failinimi: ")

def sorteeri(failinimi):
    failisisu = open(failinimi)
    lst = []
    soovitused = []
    for line in failisisu:
        puhas = line.strip()
        lst.append(puhas.split(" "))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][0] >= lst[j][0]:
                if lst[i][1] < lst[j][1]:
                    soovitused.append(lst[j])
    return soovitused

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
print(sorteeri(failinimi))
