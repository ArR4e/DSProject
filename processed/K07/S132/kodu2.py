s = float(input("Sisesta tee pikkus km: "))
f = open("taksohinnad.txt", encoding = "UTF-8")

firma_nimi = ""
odavaim_hind = 0

for rida in f:
    jupid = rida.split(",")
    sisse_hind = float(jupid[1])
    km_hind = float(jupid[2])
    kogu_hind = sisse_hind + km_hind * s
    
    if odavaim_hind == 0:
        odavaim_hind = kogu_hind
        firma_nimi = jupid[0]
        
    elif kogu_hind < odavaim_hind:
        odavaim_hind = kogu_hind
        firma_nimi = jupid[0]
        
print(f"Kõige odavam on {firma_nimi}")

f.close()
    