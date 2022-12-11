#taksohinnad
#mirjampirn
pikkus=float(input("Sisesta sõidu pikkkus kilomeetrites: "))

hinnad=open("taksohinnad.txt")
nimi=""
hind=0
kokkuhind=10000000
for row in hinnad:
    el=row.split(",")
    sisseastumine=float(el[1])
    km_hind=float(el[2])
    koguhind=sisseastumine+pikkus*km_hind
    if koguhind<kokkuhind:
        kokkuhind=koguhind
        nimi=el[0]
   
print("Kõige odavam on "+nimi+".")