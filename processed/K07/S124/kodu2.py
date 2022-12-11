teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

def odavaim_hind(teepikkus):
    if teepikkus == 0:
        return str("")
    fail = open("taksohinnad.txt", encoding = "UTF-8")
    hinnad = []
    firmad = []
    for rida in fail:
        korras_rida = rida.split(",")
        firma = korras_rida[0]
        alustustasu = float(korras_rida[1])
        kilomeetrihind = float(korras_rida[2])
        hind = float(alustustasu) + float(kilomeetrihind * teepikkus)
        hinnad += [hind]
        firmad += [firma]
        madalaim_hind = min(hinnad)
        korra_number = (hinnad.index(madalaim_hind))    
            
    fail.close()
        
    return firmad[korra_number]
        
print("Kõige odavam on", odavaim_hind(teepikkus) + ".")


