pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

hinnad = open("taksohinnad.txt","r")
parim_takso = ""
parim_hind = -1.0
for rida in hinnad:
    andmed = rida.split(",")
    praegu_hind = float(andmed[1]) + float(andmed[2]) * pikkus
    if parim_hind == -1.0 or praegu_hind < parim_hind:
        parim_takso = andmed[0]
        parim_hind = praegu_hind
hinnad.close()

print("Kõige odavam on " + parim_takso + ".")