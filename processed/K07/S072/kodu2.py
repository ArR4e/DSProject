import os

kilomeetrid = float(input("Palun sisestage tee pikkus kilomeetrites: "))

with open("taksohinnad.txt", "r") as f:
    if os.stat("taksohinnad.txt").st_size == 0:
        raise(Exception("tühi sisend!"))
    
    esimene = f.readline().strip().split(',')
    odavaim_nimi = esimene[0]
    odavaim_hind = float(esimene[1]) + kilomeetrid * float(esimene[2])
    
    for line in f:
        line_split = line.strip().split(',')
        hind = float(line_split[1]) + kilomeetrid * float(line_split[2])
        if hind < odavaim_hind:
            odavaim_hind = hind
            odavaim_nimi = line_split[0]
    
print(f"Kõige odavam on {odavaim_nimi}") 
