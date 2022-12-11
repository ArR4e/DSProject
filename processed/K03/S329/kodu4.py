fail = open("kinganumbrid.txt")

for rea in fail:
    try:
        jalasuurus = float(rea)
        pikkus = (round((2 / 3) * (jalasuurus - 2)))
        print(pikkus)      
    except:
        print("vigane rida")

fail.close()