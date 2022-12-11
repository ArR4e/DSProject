f = open("taksohinnad.txt", encoding = "utf-8")

teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
käesolev_hind = 0
odavaim_hind = 0
odavaim = ""

for rida in f:
    rida_j = rida.strip().split(",")
    käesolev_hind = float(rida_j[1]) + float(rida_j[2]) * teepikkus
    if odavaim_hind == 0:
        odavaim = rida_j[0]
        odavaim_hind = käesolev_hind
    elif käesolev_hind < odavaim_hind:
        odavaim = rida_j[0]
        odavaim_hind = käesolev_hind

if odavaim == "":
    print("Taksod puuduvad.")
else:
    print("Kõige odavam on " + odavaim + ".")

f.close()