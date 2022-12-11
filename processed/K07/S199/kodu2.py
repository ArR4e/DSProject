pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", "r")

taksode_hinnad = []
nimed = []

for rida in f:
    rida = rida.strip().split(",")
    nimi = rida[0]
    sisseistumise_hind = float(rida[1])
    km_hind = float(rida[2])
    summa = sisseistumise_hind + pikkus * km_hind
    taksode_hinnad += [summa]
    nimed += [nimi]
f.close()

indeks = 0
miinimum = taksode_hinnad[0]
for i in range(len(taksode_hinnad)):
    if taksode_hinnad[i] < miinimum:
        miinimum = taksode_hinnad[i]
        indeks = i
        
nimi = nimed[indeks]

print("Kõige odavam on "+nimi+".")
