fail = open("kinganumbrid.txt")
try:
    for rida in fail:
        kinganr = float(rida.strip())
        pikkus = (2/3 * (kinganr - 2))
        arv = round(pikkus)
        print(arv)
except:
    print("Vigane sisend")