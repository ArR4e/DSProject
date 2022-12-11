f = open("kinganumbrid.txt", "r")

kinganumbrid = f.readlines()

for i in kinganumbrid:
    try:
        i = float(i)
        pikkus = 2/3*(i-2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
