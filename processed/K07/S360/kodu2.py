kilomeetrid = float(input("Sisesta tee pikkus koju kilomeetrites: "))

f = open("taksohinnad.txt", encoding="UTF-8")

for rida in f:
    rida = rida.split(",")
    nimi = rida[0]
    stardihind = float(rida[1])
    km_hind = float(rida[2])
    
hind = stardihind + km_hind*kilomeetrid


