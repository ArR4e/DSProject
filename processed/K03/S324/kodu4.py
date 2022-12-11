fail = open("kinganumbrid.txt")

for rida in fail:
    try:
        kinganr = float(rida.strip())
        pikkus = (2/3) * (kinganr - 2)
        print(round(pikkus))
    
    except:
        print("Vigane sisend")
        

fail.close()