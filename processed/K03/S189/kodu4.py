tekst = open("kinganumbrid.txt", "r")

for i in tekst:
    try:
        pikkus = (2/3) * (float(i) - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")