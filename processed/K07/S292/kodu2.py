import math

f = open("taksohinnad.txt")

hinnad = []

for takso in f:
    hinnad.append(takso.strip().split(","))
       
f.close()

print(hinnad)

sisse = float(input("Sisesta tee pikkus kilomeetrites: "))

hind = math.inf
takso = ""

for pakkuja in hinnad:
    teenus = float(pakkuja[1])+float(pakkuja[2])*sisse
    if teenus < hind:
        hind = teenus
        takso = pakkuja[0]
        
print("Kõige odavam on", takso+".")