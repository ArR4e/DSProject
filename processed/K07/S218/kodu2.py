
f = open("taksohinnad.txt")

#Esmalt leian vähima väärtuse, millega järgmisi võrrelda
tee = float(input("Sisesta teepikkus kilomeetrites: "))

f = open("taksohinnad.txt")
rida1 = f.readline()

#kuna automaatkontrollis esines näide, kus fail oli tühi, lisasin selle jaoks eraldi kontrollause.
if rida1 == "":
    print("")
else:
    
    
    ilma_reavahetuseta = rida1.strip()
    järjend1 = (ilma_reavahetuseta.split(","))
    nimi = järjend1[0]
    hind = float(järjend1[1]) + float(järjend1[2])*tee
    seni_vähim = hind
    seni_vähim_firma = nimi
    f.close()
    
    f = open("taksohinnad.txt")
    
    for rida in f:
        
        ilma_reavahetuseta = rida.strip()
        järjend = (ilma_reavahetuseta.split(","))
        nimi = järjend[0]
        hind = float(järjend[1]) + float(järjend[2])*tee
        
        if hind < seni_vähim:
            seni_vähim = hind
            seni_vähim_firma = nimi
    f.close()
    
    print("Kõige odavam on ", seni_vähim_firma)
    
