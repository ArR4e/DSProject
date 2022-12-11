f=open("taksohinnad.txt", encoding="UTF-8")

teepikkus=float(input("Sisesta tee pikkus kilomeetrites: "))
hinnad=[ ]
nimed=[ ]
for rida in f:
    takso_andmed=(rida).split(",")
    nimi=takso_andmed[0]
    sisseistumise_hind=float(takso_andmed[1])
    km_hind=float(takso_andmed[2])
    hind=km_hind*teepikkus + sisseistumise_hind
    hinnad.append(hind)
    nimed.append(nimi)
    
väikseim=min(hinnad)
i=hinnad.index(väikseim)
odavaim=nimed[i]

print("Kõige odavam on ", odavaim)
f.close()