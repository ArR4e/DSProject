tee_pikkus = input("Sisesta teepikkus kilomeetrites: ")

f = open("taksohinnad.txt", encoding = "UTF-8")

parim_hind = 0
parim_valik = ""

for rida in f:
    jupid = rida.split(",")
    takso_nimi = jupid[0]
    sisseastumis_hind = jupid[1]
    km_hind = jupid[2]
    praegune_hind = float(sisseastumis_hind) + float(km_hind) * float(tee_pikkus)
    #print(takso_nimi)
    #print(sisseastumis_hind)
    #print(km_hind)
    #print(takso_nimi + str(hind))
    if not parim_hind:
        parim_hind = praegune_hind
        parim_valik = takso_nimi
    elif parim_hind >= praegune_hind:
        parim_hind = praegune_hind
        parim_valik = takso_nimi
        
print("Kõige odavam on", parim_valik +".")    
f.close()
    