fail = open('taksohinnad.txt','r')
kilomeetreid = float(input("Sisestage tee pikkus kilomeetrites: "))
tasu1= 0
sõidutaja =""
for rida in fail:
    andmed = rida.strip().split(",")
    nimi=andmed[0]
    sisseistumise_hind = float(andmed[1])
    kilomeetri_hind = float(andmed[2])
    tasu = sisseistumise_hind + kilomeetri_hind * kilomeetreid
    
    if tasu < tasu1 or tasu1 == 0:
        tasu1 = tasu
        sõidutaja = nimi

print("Kõige odavam on " + sõidutaja + ".")
         
fail.close()