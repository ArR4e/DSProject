import math
teepikkus = float(input("Sisestage kodutee pikkus (km): "))

f = open("taksohinnad.txt", "r", encoding = "UTF-8")

odav_hind = math.inf
for rida in f:
    rida = rida.strip().split(",")
    firma = rida[0]
    sisseistumine = rida[1]
    km = rida[2]
    hind = float(sisseistumine) + float(km)*teepikkus
    
    if hind < odav_hind:
        odav_hind = hind
        kõige_odavam = firma

print("Kõige odavam on " + kõige_odavam + ".")
f.close
    
    
    
    

 
        