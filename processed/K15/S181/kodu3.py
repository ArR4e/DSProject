file = input("Sisesta failinimi: ")
file = "sõiduplaan.txt"
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

bussiajad = []
sobivad_ajad = []
with open(file, encoding="utf-8") as f:
    f = f.read().splitlines()
    for i in f:
        i = i.split(" ")
        bussiajad.append(i)
    for x in bussiajad:
        sobivus = True
        for y in bussiajad:
            if x[0] < y[0] and x[1] > y[1] and float(x[2]) > float(y[2]):
                sobivus = False
        if sobivus:
            sobivad_ajad.append(x)
    sobivad_ajad.sort()
    for i in sobivad_ajad:
        i = " ".join(i)
        print(i)