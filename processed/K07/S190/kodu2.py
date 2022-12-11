teepikkus = float(input("Sisesta teepikkus kilomeetrites: "))

i = 0
odavaim_hind = -1
odavaim_takso = ""
fail = open("taksohinnad.txt")
for rida in fail:
    
    uus_järjend = rida.split(",")
    
    takso_nimi = uus_järjend[0] 
    sisse_hind = float(uus_järjend[1])
    km_hind = float(uus_järjend[2])
        
    kokku_hind = teepikkus * km_hind + sisse_hind
        
    if kokku_hind < odavaim_hind or odavaim_hind == -1:
        odavaim_hind = kokku_hind
        odavaim_takso = takso_nimi
    
print("Kõige odavam on" + odavaim_takso)
    
fail.close()
    

