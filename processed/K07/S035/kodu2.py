def takso_hind(järjend):
    hind=float(järjend[1])+float(järjend[2])*s
    return (hind)

s=float(input("Sisesta tee pikkus kilomeetrites: "))    
f=open("taksohinnad.txt", encoding="utf-8")
odavaim=99999
for rida in f:
    rida=rida.replace("\n", "")
    takso=rida.split(",")
    a=takso_hind(takso)
    if a<odavaim:
        odavaim=a
        odavaim_takso=("Kõige odavam on " + takso[0] + ".")
print(odavaim_takso)
