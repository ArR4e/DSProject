pikkus = int(input("Sisesta elektriliini pikkus: "))
while True:
    kaugus = int(input("Sisesta elektriliini postide max kaugus: "))
    if(pikkus>kaugus):
        break
arv = pikkus//kaugus
viga = pikkus%kaugus
if viga>0:
    arv = arv + 1
print("Postide arv on ", arv)