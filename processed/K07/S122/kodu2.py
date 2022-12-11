import math

f = open("taksohinnad.txt", encoding="UTF-8")

s = float(input("Sisesta tee pikkus kilomeetrites: "))

i=0
odavam = math.inf
while True:
    rida = f.readline()
    if rida == "":
        break
    else:
        rida = rida.split(",")
        km_hind = float(rida[2])
        alustustasu = float(rida[1])
        transport = rida[0]
        taksoteenuse_hind = float(s * km_hind + alustustasu)
        if odavam >= taksoteenuse_hind:
            odavam = taksoteenuse_hind
            odavaim_viis = transport
        i+=1
        
print("Kõige odavam on", odavaim_viis,".")
    
f.close()