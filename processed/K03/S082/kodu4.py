a = open("kinganumbrid.txt", "r")

for x in a:
    
    
    try:
        
        x=float(x)
        pikkus = 2/3 * (x - 2)
        

        print(round(pikkus))
        
    except:
        print("Vigane sisend")
        