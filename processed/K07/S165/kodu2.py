tee_pikkus = float(input("Palun sisestage tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt")
uus_hind = 1000000
odavaim = '"faili sisu tühi"'


for rida in f:
    rida = rida.split(",")
    hind = float(rida[1]) + float(rida[2]) * tee_pikkus    
    
    if hind < uus_hind:
        uus_hind = hind
        odavaim = rida[0]
    



print("Kõige odavam on", str(odavaim) + ".")
    







f.close()







