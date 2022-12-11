f = open('kinganumbrid.txt')

while True:
    sisu = f.readline()
    if sisu == "":
        break
    else:
        try:  
            kinganumber = float(sisu.strip())
            pikkus = round(2/3 * (kinganumber - 2))
            print(pikkus)
        except:
            print("Vigane sisend")   
       
f.close()