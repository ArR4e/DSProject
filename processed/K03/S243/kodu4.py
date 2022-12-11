#Erindite püüdmine failist lugemisel
f=open('kinganumbrid.txt')

while True:
    rida=f.readline()
    if rida=="":
        break
    try:
        number=float(rida.strip())
        pikkus=2/3*(number-2)
        vastus=round(pikkus)
        print(vastus)
    except:
        print("Vigane sisend")

f.close()