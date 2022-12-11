distants = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", "r")

väikseim = 999999
odavaim_firma = "takso tellimata jätta"

while True:
    
    rida = f.readline().strip()
    
    if rida == "":
        break
    
    elif distants == 0:
        print("Sul pole taksot vajagi :)")
        break
    
    else:
    
        jupid = rida.split(",")
        
        hind = float(jupid[1]) + distants*float(jupid[2]) 
            
        if hind <= väikseim:
                väikseim = hind
                odavaim_firma = jupid[0]
                
print("Kõige odavam on ", odavaim_firma, '.', sep='')       

f.close()