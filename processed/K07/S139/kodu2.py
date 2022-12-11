f = open("taksohinnad.txt", encoding= "UTF-8")
teepikkus = float(input("Sisesta teepikkus kilomeetrites: "))
hind = None
parim_takso = None
for rida in f:
    takso = rida.strip().split(",")
    uus_hind = float(takso[1])+(teepikkus*float(takso[2]))
    if hind == None:
        hind = uus_hind
        parim_takso = takso[0]
    elif uus_hind < hind:
        hind = uus_hind
        parim_takso = takso[0]
print("Kõige odavam on " + parim_takso)
    
f.close()