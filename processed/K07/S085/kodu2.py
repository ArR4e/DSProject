tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding="UTF-8")
hinnad = []
nimed = []
for rida in f:
    jupid = rida.split(",")
    taksonimi = jupid[0]
    stardihind = jupid[1]
    kilomeetri_tasu = jupid[2].strip()
    hind = float(stardihind) + tee_pikkus * float(kilomeetri_tasu)
    hinnad.append(hind)
    nimed.append(taksonimi)
if hinnad != []:
    indeks = 0
    miinimum = hinnad[0]
    for i in range(len(hinnad)):
        if hinnad[i] <= miinimum:
            miinimum = hinnad[i]
            indeks = i
    print("Kõige odavam on ", nimed[indeks])
f.close()