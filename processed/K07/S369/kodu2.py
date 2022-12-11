import os

def taksohind():
    tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
    
    f = open("taksohinnad.txt")
    
    if os.path.getsize("taksohinnad.txt") == 0:
        return
    else:
        
        taksode_hinnad = []
        taksode_nimed = []
        for line in f:
            km_hind = float(line.strip().split(',')[2])
            start_hind = float(line.strip().split(',')[1])
            nimi = line.strip().split(',')[0]
            hind = (start_hind + tee_pikkus*km_hind)
            
            taksode_nimed.append(nimi)
            taksode_hinnad.append(hind)
            
        
        
        odavaim = min(taksode_hinnad)
        indeks = taksode_hinnad.index(odavaim)
        odavaim_nimi = taksode_nimed[indeks]
        print("Koige odavam on ",odavaim_nimi)
        
    f.close()
     
taksohind()
    