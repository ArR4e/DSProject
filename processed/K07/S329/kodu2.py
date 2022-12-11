# 2. Taksohinnad

kilomeetrite_arv = float(input("Sisesta tee pikkus kilomeetrites: "))
n = 0
taksode_hinnad = []
nimed = []

fail = open("taksohinnad.txt", "r", encoding = "UTF-8")
for rida in fail:
    n = n + 1
    b = rida.split(",")
    nimi = (b[0])
    stardihind = float(b[1])
    kilomeetri_tasu = float(b[2])
    hind = stardihind + kilomeetrite_arv * kilomeetri_tasu
    taksode_hinnad.append(hind)
    nimed.append(nimi)

if n == 0:
    print("Teie tekstifailis pole midagi!")
else:
    väikseim = min(taksode_hinnad)
    indeks = taksode_hinnad.index(väikseim)
    name = nimed[indeks]
    print("Kõige odavam on ", name, ".", sep="")
