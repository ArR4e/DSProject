nrid = open("kinganumbrid.txt", "r").readlines()
for rida in nrid:
    try:
        print(round(2/3 * (float(rida) - 2)))
    except:
        print("Vigane sisend")
