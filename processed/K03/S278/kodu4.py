fail = open("kinganumbrid.txt", "r+")

for rida in fail:
    try:
        kinganumber = float(rida.strip())
        jalalabaPikkus = round(2/3 * (kinganumber - 2))
        print(jalalabaPikkus)
    except:
        print("Vigane sisend")
        
fail.close()