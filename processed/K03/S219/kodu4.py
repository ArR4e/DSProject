f = open("kinganumbrid.txt", "r")

while True:
    try:
        for rida in f:
            x = float(rida.strip())
            pikkus = ((2/3) * (x - 2))
            print(round(pikkus))
        
    except:
        print("Vigane sisend")
        continue
    
    
    