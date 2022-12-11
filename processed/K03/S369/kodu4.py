f = open("kinganumbrid.txt")

for line in f:
    try:
        kinganumber = float(line.strip())
        pikkus = round((kinganumber - 2) * (2/3))
        print(pikkus)
    
    except:
        print("Vigane sisend")
    
    
    
    
    
    
