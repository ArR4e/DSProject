kilomeetrite_arv = float(input("Palun sisestage tee pikkust(km):  "))
teepikkus = 0
hinnad = []
nimetused = []



fail = open("taksohinnad.txt" , "r", encoding = "UTF-8")
for rida in fail:
    teepikkus = teepikkus + 1
    andmed = rida.split(",")
    takso_nimi = (andmed[0])
    stardihind = float(andmed[1])
    kilomeetri_hind = float(andmed[2])
    hind = stardihind + kilomeetrite_arv * kilomeetri_hind
    hinnad.append(hind)
    nimetused.append(takso_nimi)

if teepikkus == 0:
    print("Tühi hinnakiri")
else:
    odavam = min(hinnad)
    indeks= hinnad.index(odavam)
    name = nimetused[indeks]
    print("Kõige odavama taksofirma: ",name , ".", sep="")


    
    