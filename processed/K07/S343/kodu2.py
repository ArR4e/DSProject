f=open("taksohinnad.txt", encoding="UTF-8")
sisu=f.readlines()
teepikkus=float(input("Sisesta teepikkus"))
hind=[]
teenus=[]

try:
    for line in sisu:
    
        x = line.strip().split(",")
        hind+=[teepikkus*float(x[2])+float(x[1])]
        teenus+=[x[0]]
    print("Kõige odavam on", str(teenus[hind.index(min(hind))])+ ".")
except:
    if teepikkus == 0:
        print("Odavaim takso on .")
f.close()