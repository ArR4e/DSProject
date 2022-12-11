f = open("kinganumbrid.txt")

for rida in f:
    try:
        sisu = float(rida.strip())
        rida = 2/3 * (sisu - 2)
        rida = round(rida)
        print (rida)
    except:
        print("Vigane sisend")
        
f.close()