f=open("taksohinnad.txt", "r")
andmed=list(f.read().replace("\n", ",").split(","))
def odavaim(km):
    n=0
    odavaimfirma=""
    odavaimhind=float(999999999)
    while n<len(andmed):
        nimi=andmed[n]
        n+=1
        sissehind=float(andmed[n])
        n+=1
        kmhind=float(andmed[n])
        n+=1
        hind= km*kmhind + sissehind
        if hind<odavaimhind:
            odavaimhind=hind
            odavaimfirma=nimi
    return odavaimfirma

pikkus=float(input("Sisesta tee pikkus kilomeetrites :"))
print("Kõige odavam on " + odavaim(pikkus) + ".")

        
