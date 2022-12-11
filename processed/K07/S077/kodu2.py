teepikkus=float(input("Sisesta tee pikkus kilomeetrites: "))

f=open("taksohinnad.txt", encoding="UTF-8")

rida=f.readline()
takso=rida.strip().split(",")        
odavaim=float(takso[1])+teepikkus*float(takso[2])
nimi=takso[0]

for rida in f:
    takso=rida.strip().split(",")
    hind=float(takso[1])+teepikkus*float(takso[2])
    if hind<odavaim:
        odavaim=hind
        nimi=takso[0]
    
f.close()

print("Kõige odavam on võtta",nimi+".")

