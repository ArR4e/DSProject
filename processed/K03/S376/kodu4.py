fail = open("kinganumbrid.txt")

for rida in fail:
    try:
        kinganr = float(rida.strip())
        pikkus = 2/3 * (kinganr - 2)
        ümardatud_pikkus = round(pikkus)
        print(int(ümardatud_pikkus))
    except:
        print("Vigane sisend")