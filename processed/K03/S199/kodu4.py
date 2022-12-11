f = open("kinganumbrid.txt")
for rida in f:
    kinganumber = round(float(rida.strip()))
    try:
        kinganumber = round(float(rida.strip()))
        pikkus = 2/3 * (kinganumber - 2)
        print(pikkus)
    except:
        print("Vigane sisend") 

