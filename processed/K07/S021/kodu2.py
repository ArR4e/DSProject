f = open("taksohinnad.txt", encoding = "UTF-8")
teepikkus = float(input("Sisestage tee pikkus kilomeetrites: "))

seni_odavaim = None
odavaim = ""
for rida in f:
    järjend = rida.strip().split(",")
    sisseastumise_hind = järjend[1]
    kilomeetri_hind = järjend[2]
    hind = teepikkus*float(kilomeetri_hind)+float(sisseastumise_hind)
    if seni_odavaim == None or hind < seni_odavaim:
        seni_odavaim = hind
        odavaim = järjend[0]
    else:
        continue
    
print("Kõige odavam on " + odavaim)

f.close()