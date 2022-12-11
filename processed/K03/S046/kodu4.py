file = open("kinganumbrid.txt", "r")
for rida in file:
    kinganumber = rida.strip("\n")
    try:
        pikkus = 2/3 * (float(kinganumber) - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
    