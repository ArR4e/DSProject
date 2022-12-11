f = open("kinganumbrid.txt")


for rida in f:

    while True:
        try:
            kinganr = float(rida.strip())
            pikkus = round(2/3 * (kinganr - 2))
            print(pikkus)
            break
        except:
            print("Vigane sisend :(")
            break
    
