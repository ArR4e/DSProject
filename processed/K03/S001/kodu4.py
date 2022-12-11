kinganumbrid = open("kinganumbrid.txt", "r")

for rida in kinganumbrid:
    try:
        jalg = round(2 / 3 * (float(rida) - 2))
        print(jalg)
    except:
        print("Vigane sisend")

kinganumbrid.close()