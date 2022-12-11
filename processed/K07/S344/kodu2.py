km = float(input("Sisesta tee pikus kilomeetrites: "))

odavaim_hind = 0
odavaim_nimi = ""
f = open("taksohinnad.txt")
for rida in f:
    jupid = rida.split(",") 
    nimi = jupid[0]
    sisseistumise_hind = jupid[1]
    kilomeetri_hind = jupid[2]
    hind = float(kilomeetri_hind) * km + float(sisseistumise_hind)
    if odavaim_hind == 0 or hind < odavaim_hind:
        odavaim_hind = hind
        odavaim_nimi = nimi
        
print("Kõige odavam on: ", odavaim_nimi)