f=open("taksohinnad.txt",encoding="UTF-8")
sisu=f.readlines()
f.close()
pikkus=float(input("Sisesta tee pikkus koju kilomeetrites"))
odavaim="pole veel"
for a in range(len(sisu)):
    sisu[a]=sisu[a].split(",")
    maksumus=float(sisu[a][1])+pikkus*float(sisu[a][2])
    if odavaim=="pole veel":
        odavaim=maksumus
        vastus=sisu[a][0]
    if maksumus<=odavaim:
        odavaim=maksumus
        vastus=sisu[a][0]
try:
    print("Odavaim takso on",vastus+".")
except:
    print("")