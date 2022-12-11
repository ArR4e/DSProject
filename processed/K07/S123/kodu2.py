taksode_hinnad=[]
hind=[]
nimi=[]

s=float(input("Sisesta teepikkus koju: "))

f=open("taksohinnad.txt", encoding="UTF-8")
sisu=f.readlines()
try:
    for rida in sisu:
        x=rida.strip().split(",")
        hind=float(x[1])+s*float(x[2])
        taksode_hinnad+=[hind]
        nimi+=[x[0]]    
    
    nimi = nimi[taksode_hinnad.index(min(taksode_hinnad))]

    print("Kõige odavam on", nimi + ".")
except:
    if s==0:
        print("Kõige odavam on", ".")
    
f.close()
