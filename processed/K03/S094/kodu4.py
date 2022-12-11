file = open("kinganumbrid.txt", "r")

for rida in file:
    try:        
        kinganumber = float(rida.strip())
        pikkus = 2/3 * (kinganumber - 2)
        pikkusr = round(pikkus)
        str(print(pikkusr))

    except:
        print("Vigane sisend")

