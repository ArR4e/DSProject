f = open("taksohinnad.txt", encoding = "UTF-8")

km = float(input("Sisestage kilomeerite arv: "))

odavaim = 0
takso_nimi = ""

for rida in f:
    uusrida = rida.strip()
    
    km_hind = float(uusrida.split(",")[-1])
    alustasu = float(uusrida.split(",")[-2])
    
    hind = alustasu + km_hind * km
    
    if odavaim == 0 and odavaim < hind:
        takso_nimi = uusrida.split(",")[-3]
        odavaim = hind
        
    elif odavaim > hind:
        takso_nimi = uusrida.split(",")[-3]
        odavaim = hind
        
print("Kõige odavam on", takso_nimi + ".")

f.close()
    