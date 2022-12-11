fail = open("kinganumbrid.txt")

for rida in fail :
    try:
        kinganumber = float(rida)
        pikkus = round(2 / 3 * (kinganumber - 2 ))
        print (pikkus)
        
    except:
        print ("vigane sisend")
        
fail.close()