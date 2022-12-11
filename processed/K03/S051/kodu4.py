f = open("kinganumbrid.txt")

for i in f:
    try:
        kinganr = float(i)
        jala_pikkus = 2/3 * (kinganr - 2)
        print(round(jala_pikkus))
    except:
        print("Vigane sisend")