import math
f=open("taksohinnad.txt",encoding="UTF-8")
teepikkus=float(input("Sisesta tee pikkus kilomeetrites: "))
odavam=float("inf")
koht=""

for rida in f:
    a=rida.split(",")
    hind=float(a[-1])*teepikkus+float(a[-2])
    if hind<odavam:
        odavam=hind
        koht=a[:-2]
    else:
        pass
    
if koht=="":
    print("")
else:
    print("Kõige odavam on "+ " ".join(koht)+".")

f.close()