f=open("taksohinnad.txt", encoding="UTF-8")
pikkus=float(input("Sisesta sõidu pikkus kilomeetrites:"))
soodsaim=""
shind=-1
for rida in f.readlines():
    jupid=rida.split(",")
    takso=jupid[0]
    iste=float(jupid[1])
    km=float(jupid[2])

    tee=pikkus*km+iste
    if tee<shind or shind==-1:
        soodsaim=takso
        shind=tee

print("Kõige odavam on:",soodsaim)

f.close()