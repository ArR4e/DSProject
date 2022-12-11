f = open("taksohinnad.txt", encoding = "utf-8-sig")
vahemaa = float(input("Sisesta tee pikkus kilomeetites:"))
suurimkoguhind = 0
nimed = []
koguhinnad = []
while True:
    rida = f.readline().strip()
    takso_järjend = rida.split(",")
    if rida =="":
        break
    nimi = takso_järjend[0]
    sisseastumine = float(takso_järjend[1])
    kilomeetrihind = float(takso_järjend[2])
    koguhind = vahemaa*kilomeetrihind + sisseastumine
    koguhinnad.append(koguhind)
    nimed.append(nimi)
    indeks = 0
    miinimum = koguhinnad[0]
    for x in range(len(koguhinnad)):
        if koguhinnad[x] < miinimum:
            miinimum = koguhinnad[x]
            indeks = x
print("Kõige odavam on "+ str(nimed[indeks]))
f.close()