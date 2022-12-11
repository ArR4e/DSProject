fail = open("taksohinnad.txt", "r")
kilomeetrite_arv = int(input("Sisesta tee pikkus kilomeetrites: "))
pikkus = len(fail.readlines())
fail.close()
fail = open("taksohinnad.txt", "r")
nimed = []
hinnad = []
for i in range(pikkus):
    for rida in fail:
        nimi = str(rida.split(",")[0])
        stardihind = float(rida.split(",")[1])
        kilomeetri_tasu = float(rida.split(",")[2])
        hind = stardihind + kilomeetrite_arv*kilomeetri_tasu
        nimed.append(nimi)
        hinnad.append(hind)

indeks = 0
miinimum = hinnad[0]
for i in range(len(hinnad)):
    if hinnad[i] <= miinimum:
        miinimum = hinnad[i]
        indeks = i
        
print("Kõige odavam on" , nimed[indeks])






