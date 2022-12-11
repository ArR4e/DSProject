s=float(input("Sisesta tee pikkus kilomeetrites: "))
f=open("taksohinnad.txt", encoding="UTF-8")
hind=float("inf")
nimi=""
for i in f:
    a=i.split(",")
    algus=float(a[1])
    km=float(a[2])
    kokku=algus+km*s
    if kokku<hind:
        hind=kokku
        nimi=a[0]
print(f"Kõige odavam on {nimi}.")
f.close()