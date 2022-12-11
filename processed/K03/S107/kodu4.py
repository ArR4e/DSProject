f = open("kinganumbrid.txt")
kinganumbrid = f.readlines()
f.close

for rida in kinganumbrid:
    
    try:
        kinganumbrid = float()
        rida = float(rida.strip())
        pikkus = round(2/3 * (rida - 2))
        print(pikkus)
    except:
        print("Vigane sisend")
        


        
        
