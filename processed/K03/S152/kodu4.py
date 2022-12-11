f = open("kinganumbrid.txt", "r")
for kinganr in f:
    try:
        pikkus = 2/3*int(float(kinganr.strip())-2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
        