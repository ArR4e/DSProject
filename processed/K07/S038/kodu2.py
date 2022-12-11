pikkus = input("Sisestage tee pikkus kilomeetrites:")
fail=open("taksohinnad.txt")
algus = 0.0
kmhind = 0.0
hind = 100.0
for rida in fail:
    uus= rida.split(",")
    algus = uus[-2]
    kmhind = uus[-1]
    u_hind = float(algus)+ float(kmhind)*float(pikkus)
    if u_hind < hind:
        hind = u_hind
        valik = uus[-3]
    
print("Kõige odavam on",valik)
        
    