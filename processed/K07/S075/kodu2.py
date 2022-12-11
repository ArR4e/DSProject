import math
f=open("taksohinnad.txt", encoding="UTF-8")
pikkus=float(input("Sisesta tee pikkus kilomeetrites: "))
odavam=float("inf")
koht=""

for takso in f:
    jupid=takso.split(",")
    maksab=float(jupid[-1])*pikkus+float(jupid[-2])
    if maksab<odavam:
        odavam=maksab
        koht=jupid[:-2]
    else:
        pass

if koht=="":
    print("")
else:
    print("Kõige odavam on "+ " ".join(koht)+".")

f.close()