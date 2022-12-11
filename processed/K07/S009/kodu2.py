def koju_soit(km):
    taksod = []
    sisenemised = []
    km_hinnad = []
    
    f = open('taksohinnad.txt', encoding='UTF-8')
    for rida in f:
        osad = rida.split(',')
        takso = osad[0]
        sisenemine = osad[1]
        km_hind = osad[2]
        taksod = taksod + [takso]
        sisenemised = sisenemised + [sisenemine]
        km_hinnad = km_hinnad + [km_hind]
    f.close()
    
    return (taksod, sisenemised, km_hinnad)
    
    for takso_soovitus in range(km):
        hind = km_hinnad * km + sisenemised
        #ei tea kuhu edasi joosta sellega, kõik tundub vale
        
        indeks = 0
        miinimum = taksod[0]
        for i in range(len(taksod)):
            if taksod[i] < miinimum:
                miinimum = taksod[i]
                indeks = i
        
km = float(input("Palun sisesta kodutee kilomeetrites: "))

print("Koju on kõige targem minna taksoga " + taksod[i])    