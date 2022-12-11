# encoding - UTF8: täpitähed

km_arv = float(input("Sisesta tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt", encoding="UTF-8")

odavaim = 0
for rida in fail:
    taksod = rida.strip().split(",")
    start = taksod[1]
    km_tasu = taksod[2]
    hind = float(km_arv) * float(km_tasu) + float(start)
    if hind < odavaim < odavaim or odavaim == 0:
        odavaim = hind
        odavaimT = taksod
        
fail.close()

print("Kõige odavam on ", odavaimT[0])

   
    
    
