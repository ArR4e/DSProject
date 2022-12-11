koju = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt")
hind2=50000000000000
takso=""
for i in f:
    jupid=i.split(",")
    nimi=jupid[0]
    sisse=float(jupid[1])
    kilomeeter=float(jupid[2].strip())
    hind=sisse+kilomeeter*koju
    if hind < hind2:
        takso=nimi
        hind2=hind
    elif hind > hind2:
        hind2=hind2
    
print("kõige odavam on: "+takso)
f.close()
