kilomeetrite_arv =float(input("Sisestage teepikkus koju kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "UTF-8")
taksode_hinnad = []
nimed =[]

for rida in f:
    read = rida.strip("\n")
    uus_rida = rida.split(",")
    firma = uus_rida[0]
    stardihind = float(uus_rida[1])
    kilomeetri_tasu= float(uus_rida[2])
    hind = (stardihind + (kilomeetrite_arv*kilomeetri_tasu))
    taksode_hinnad.append(hind)
    nimed.append(firma)
f.close()

indeks = 0
miinimum = taksode_hinnad[0]
for i in range(len(taksode_hinnad)):
    if taksode_hinnad[i]< miinimum:
        miinimum = taksode_hinnad[i]
        indeks= i
o_firma= nimed[indeks]

print(f"Kõige odavam on {o_firma}.")
   
